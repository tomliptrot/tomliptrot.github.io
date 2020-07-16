# !/usr/bin/python
import os
from pathlib import Path
from shutil import copyfile
import fire
import frontmatter
import string
import sys
from datetime import datetime

def new_newsletter(issue_number, issue_date, newsletter_folder = '_posts/newsletter/', template = '_posts/post_template.md', time_to_publish = '21:00:00'):

    newsletter_folder= Path(newsletter_folder)
    name = 'issue_' + str(issue_number)
    new_folder = newsletter_folder / name 
    new_folder.mkdir(parents=True, exist_ok=True)

    #make 5 copies of the post template
    template = Path(template)
    
    for i in range(5):
        name = issue_date + '-item' + str(i+1) + '.md'
        new_post = Path(new_folder / name)
        copyfile(template , new_post)
        post_content = frontmatter.load(template )
        post_content['story_number'] = i+1
        post_dttm = datetime.strptime(pissue_date + time_to_publish,  '%Y-%m-%d%H:%M:%S')
        post_content['date'] = post_dttm
        frontmatter.dump(post_content, new_post)


def rename(path, time_to_publish = '21:00:00'):
    path = Path(path)
    for file in path.iterdir():
        post = frontmatter.load(file)
        post_name = file.stem
        post_date = post_name[0:10] 
        story_number = str(post['story_number'])
        title = post['title']
        if(title):
            title = title.translate(str.maketrans('', '', string.punctuation))
            title = title.replace(" ", "-")
            title = title.lower()
            title = post_date + '-item-' + story_number  + '-' + title + '.md'
            file.rename(path / title )   

if __name__ == "__main__":
    fire.Fire()

