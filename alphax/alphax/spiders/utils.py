import os
import time
from datetime import datetime
from newspaper import Article

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


current_date = datetime.now().strftime("%Y-%m-%d")


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def create_directory_file(basedir, path):
    if not os.path.exists(basedir):
        os.makedirs(basedir)  # Create directory
        f = open(path, 'a')  # Create file
        f.close()


def get_domain_name(url):
    source = url.split(".")  # Get url source
    if len(source[1]) < 4:
        return source[0]
    return source[1]


def read_content(url):
    try:
        content = Article(url, keep_article_html=True)
        content.download()
        content.parse()
        time.sleep(1)

        json_ = list()
        json_.append({
            "title": content.title,
            "link": url,
            "body": content.text,
            "created_at": current_date,
            "created_parsed": content.publish_date
        })
        return json_
    except Exception as e:
        print(e)  # for the repr
        print(str(e))  # for just the message
        print(e.args)
        return None
