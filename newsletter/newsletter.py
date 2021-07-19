# !/usr/bin/python
import os
from pathlib import Path
from shutil import copyfile
import fire
import frontmatter
import urllib
import string
import sys
from datetime import datetime
from urllib import request
from bs4 import BeautifulSoup
from bs4.element import Comment
from timefhuman import timefhuman
import webbrowser
import typer
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import markdown2
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
mailchimp_key = os.environ.get("MAILCHIMP_API_KEY")


def get_title(url):
    print(url)
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        html = request.urlopen(req).read().decode("utf8")
    except urllib.error.HTTPError:
        return "null"
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title")
    for text in soup.find_all("text"):
        # Here you do whatever you want with text
        print(text)
    return title.string


def tag_visible(element):
    if element.parent.name in [
        "style",
        "script",
        "head",
        "title",
        "meta",
        "[document]",
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, "html.parser")
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return " ".join(t.strip() for t in visible_texts)


def get_word_count(url):
    print(url)
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        html = request.urlopen(req).read().decode("utf8")
        text = text_from_html(html)
        # Here you do whatever you want with text
        words = text.split()
        return f"{len(words):,}"
    except UnicodeDecodeError:
        return "null"
    except urllib.error.HTTPError:
        return "null"


def get_last_issue_number(
    newsletter_folder="_posts/newsletter/",
):
    newsletter_folder = Path(newsletter_folder)
    previous_issues = [
        int(f.name.replace("issue_", ""))
        for f in newsletter_folder.glob("issue_[0-9]*")
    ]
    return max(previous_issues)


def combine(
    issue_number=get_last_issue_number(), newsletter_folder="_posts/newsletter/"
):
    newsletter_folder = Path(newsletter_folder)
    name = "issue_" + str(issue_number)
    issue_folder = newsletter_folder / name
    outfile = Path("_posts/newsletter/full_issues/") / (name + ".md")
    if outfile.exists():
        outfile.unlink()
    combined = []
    for file in sorted(issue_folder.iterdir()):
        post = frontmatter.load(file)
        # add a title to each post and  combine inot one markdown file
        title_of_post = f"## {post['story_number']}. {post['title']}"
        combined.append(title_of_post)
        if post["image"]:
            post_image_url = f"https://ortom.co.uk{post['image']}"
            combined.append(f"![{post['title']}]({post_image_url})")
        combined.append(post.content)
        if post.get("important"):
            combined.append(f"🛎️ **Why this matters:**{post['important']}")
        if post.get("word_count"):
            link = f"[📖 Read more ({post['word_count']} words)📖]({post['link']})\n"
        else:
            link = f"[📖 Read more 📖]({post['link']})\n"
        combined.append(link)
        combined.append("---")
    combined_string = "\n\n".join(combined)

    outfile.write_text(combined_string)
    print(combined_string)


def seperate(
    issue_number=get_last_issue_number(), newsletter_folder=Path("_posts/newsletter/")
):
    """Opposite of combine"""
    name = "issue_" + str(issue_number)
    issue_folder = newsletter_folder / name
    combined = Path("_posts/newsletter/full_issues/") / (name + ".md")
    combined_text = combined.read_text()
    combined_text = combined_text.split("---")
    for item, file in zip(combined_text, sorted(issue_folder.iterdir())):
        post = frontmatter.load(file)
        # remove first three lines
        item = item.split("\n")[3:]
        # remove last lines
        item = item[:-4]
        item = "\n".join(item)
        post.content = item
        print(item)
        frontmatter.dump(post, file)


def new_issue_details():
    issue_number = get_last_issue_number()
    newsletter_folder = Path("_posts/newsletter/")
    name = "issue_" + str(issue_number)
    issue_folder = newsletter_folder / name
    return issue_folder, issue_number


def new(
    issue_datetime=timefhuman("tuesday at 07:30"),
    issue_number=get_last_issue_number() + 1,
    newsletter_folder="_posts/newsletter/",
    template="_posts/post_template.md",
):
    # TODO: move to netlify
    newsletter_folder = Path(newsletter_folder)
    issue_name = "issue_" + str(issue_number)
    new_folder = newsletter_folder / issue_name
    new_folder.mkdir(parents=True, exist_ok=True)

    issue_date = issue_datetime.strftime("%Y-%m-%d")
    print(f"making issue number {issue_number} to be published at {issue_datetime}")
    images_folder = Path(f"assets/images/newsletter/{issue_name}")
    images_folder.mkdir(parents=True, exist_ok=True)

    # make 5 copies of the post template
    template = Path(template)

    for i in range(5):
        name = issue_date + "-item" + str(i + 1) + ".md"
        new_post = Path(new_folder / name)
        copyfile(template, new_post)
        post_content = frontmatter.load(template)
        post_content["story_number"] = i + 1
        post_dttm = issue_datetime
        post_content["date"] = post_dttm
        post_content["image"] = f"/assets/images/newsletter/{issue_name}/"
        frontmatter.dump(post_content, new_post)


def open_links(
    issue_number=get_last_issue_number(), newsletter_folder="_posts/newsletter/"
):
    newsletter_folder = Path(newsletter_folder)
    name = "issue_" + str(issue_number)
    issue_folder = newsletter_folder / name
    new = 1
    for file in issue_folder.iterdir():
        post = frontmatter.load(file)
        url = post["link"]
        webbrowser.get().open(url, new=new)
        new = 2


def rename(
    issue_number=get_last_issue_number(), newsletter_folder="_posts/newsletter/"
):
    newsletter_folder = Path(newsletter_folder)
    name = "issue_" + str(issue_number)
    issue_folder = newsletter_folder / name
    for file in issue_folder.iterdir():
        post = frontmatter.load(file)
        post_name = file.stem
        post_date = post_name[0:10]
        story_number = str(post["story_number"])
        title = post["title"]
        if not title:
            title = get_title(post["link"])
            if not title:
                title = "title"
            post["title"] = str(title)
        if not post.get("word_count"):
            post["word_count"] = str(get_word_count(post["link"]))
        title = title.translate(str.maketrans("", "", string.punctuation))
        title = title.replace(" ", "-")
        title = title.lower()
        title = f"{post_date}-item-{story_number}-{title}.md"
        frontmatter.dump(post, file)
        file.rename(issue_folder / title)


def redate(new_date):
    issue_folder, issue_number = new_issue_details()
    for file in issue_folder.iterdir():
        post = frontmatter.load(file)
        post_name = file.stem
        old_post_dttm = post["date"]
        old_post_time = old_post_dttm.strftime("%H:%M:%S")
        post["date"] = datetime.strptime(
            f"{new_date} {old_post_time}", "%Y-%m-%d %H:%M:%S"
        )
        story_number = str(post["story_number"])
        title = post["title"]
        title = f"{new_date}-item-{story_number}-{title}.md"
        frontmatter.dump(post, file)
        file.rename(issue_folder / title)


def resize_images(issue_number=get_last_issue_number()):
    image_folder = Path(f"assets/images/newsletter/issue_{issue_number}/")
    for file in image_folder.iterdir():
        im = Image.open(file)
        width, height = im.size
        if height > width / 2:
            new_height = width / 2
            height_to_crop = height - new_height
            left = 0
            right = width
            top = height_to_crop / 2
            bottom = height - (height_to_crop / 2)
            image_out = im.crop((left, top, right, bottom))
        else:
            image_out = im

        newsize = (1600, 800)
        image_out = image_out.resize(newsize)
        image_out.save(file)


def deploy(
    subject_line=None,
    campaign_id=None,
    issue_number=get_last_issue_number(),
    newsletter_folder="_posts/newsletter/",
    LIST_ID="7ecb50801c",
    TEMPLATE_ID=10020578,
):
    newsletter_folder = Path(newsletter_folder)
    name = "issue_" + str(issue_number)
    if not subject_line:
        subject_line = name
    issue_folder = newsletter_folder / name
    sections = []
    for file in sorted(issue_folder.iterdir()):
        # get content
        post = frontmatter.load(file)
        # convert to html
        # add to dict
        if post["image"]:
            post_image_url = f"https://ortom.co.uk{post['image']}"
        item = {
            "postimage1": f""" <img src="{post_image_url }" alt={post['title']} """,
            "posttext1": f"""{post['story_number']}. {post['title']}""",
            "headingdivider1": "",
            "postmaintext1": markdown2.markdown(
                post.content, extras=["fenced-code-blocks"]
            ),
            "postlink1": f'<a href="{post["link"]}" class="btn-read-more" style="text-decoration:none;">Read more</a>',
            "postcount1": f"({post['word_count']})",
            "whyimportant1": "Why is it important?",
            "whyimportanttext1": post["important"],
        }
        # add to list
        sections.append(item)

    # make new campaign
    # add content
    # see https://mailchimp.com/developer/marketing/api/campaigns/add-campaign/
    settings = {
        "subject_line": subject_line,
        "title": subject_line,
        "from_name": "Tom Liptrot",
        "reply_to": "tom@ortom.ai",
    }

    client = MailchimpMarketing.Client()
    client.set_config({"api_key": mailchimp_key, "server": "us6"})
    if not campaign_id:
        campaign = client.campaigns.create(
            {
                "type": "regular",
                "recipients": {"list_id": LIST_ID},
                "settings": settings,
            }
        )
        campaign_id = campaign["id"]

    content = {"template": {"id": TEMPLATE_ID, "sections": {"repeat_1": sections}}}
    client.campaigns.set_content(campaign_id, content)


def main():
    fire.Fire()


if __name__ == "__main__":
    main()
