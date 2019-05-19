import requests

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.helper import fetch, commit
from time import sleep

def download_image(url, filename):
    """
    Downloads image from the URL and saves onto disk.
    :param url: url to downlaod from
    :param filepath: where to save the file
    """
    filepath = os.path.dirname(os.path.abspath(__file__))+'/images/raw/'+filename
    print(filepath)
    with open(filepath, 'wb') as fp:
        r = requests.get(url)
        fp.write(r.content)

def download_images():
    SQL = """
        SELECT
            image_name,
            image_url
        FROM fashion_image_links
        LIMIT 100;
    """
    records = fetch(SQL)
    for record in records:
        download_image(record['image_url'], record['image_name'])
        sleep(0.5)

if __name__ == '__main__':
    download_images()