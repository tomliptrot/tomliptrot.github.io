# !/usr/bin/python
import os
from pathlib import Path
from shutil import copyfile
import fire
import frontmatter
import string
import sys
from datetime import datetime
from urllib import request
from bs4 import BeautifulSoup
from bs4.element import Comment


def get_title(url):
    print(url)
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = request.urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title')
    for text in soup.find_all('text'):
        # Here you do whatever you want with text
        print(text)
    return title.string 

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


def get_word_count(url):
    print(url)
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = request.urlopen(req).read().decode('utf8')
    text = text_from_html(html)
    # Here you do whatever you want with text
    words = text.split()
    return f'{len(words):,}'

def combine_newsletter_articles(path):
    path, time_to_publish = '21:00:00'):
    path = Path(path)
    out_string = ''
    for file in path.iterdir():
        post = frontmatter.load(file)
        #add a title to each post and  combine inot one markdown file
        post_md = '## ' + post_content['story_number'] + post['title']+ '\n' + post.content + '\n'
        out_string = out_string + post_m
    print(out_string)

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
        post_dttm = datetime.strptime(issue_date + time_to_publish,  '%Y-%m-%d%H:%M:%S')
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
        if not title:
            title = get_title(post['link'])
            post['title'] = str(title)

        post['word_count']  = str(get_word_count(post['link']))

        title = title.translate(str.maketrans('', '', string.punctuation))
        title = title.replace(" ", "-")
        title = title.lower()
        title = post_date + '-item-' + story_number  + '-' + title + '.md'
        frontmatter.dump(post, file)
        file.rename(path / title )   



if __name__ == "__main__":
    fire.Fire()

