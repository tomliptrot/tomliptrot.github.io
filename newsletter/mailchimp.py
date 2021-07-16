import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import pprint

LIST_ID = "7ecb50801c"
TEMPLATE_ID = 10019982


client = MailchimpMarketing.Client()
client.set_config({"api_key": "bedadac524fa35f2ab16ee25340830d3-us6", "server": "us6"})

# creat a campaign
settings = {"subject_line": "test", "from": "tom@ortom.ai"}
try:
    campaign = client.campaigns.create(
        {"type": "regular", "recipients": {"list_id": LIST_ID}, "settings": settings}
    )

    item_1 = {
        "postimage1": """ <img src="https://ortom-new.netlify.app/static/95672402a7e63306610c7e0c1ccd7a59/743b3/nick-fewings-dRCQJZoTYCc-unsplash.jpg" 
               alt="Post Picture" """,
        "posttext1": "What is the protein folding problem?",
        "headingdivider1": "",
        "postmaintext1": "abc",
        "postlink1": '<a href="#" class="btn-read-more" style="text-decoration:none;">Read more</a>',
        "postcount1": "(1,324 words)",
        "whyimportant1": "Why is it important?",
        "whyimportanttext1": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    }
    content = {
        "template": {"id": TEMPLATE_ID, "sections": {"repeat_1": [item_1, item_1]}}
    }
    client.campaigns.set_content(campaign["id"], content)
except ApiClientError as error:
    print("Error: {}".format(error.text))
