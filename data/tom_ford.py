import requests
from bs4 import BeautifulSoup

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.helper import fetch, commit
from time import sleep


# base_urls = [
#     'https://www.tomford.co.uk/men/ready-to-wear/knitwear/'
# ]

# for url in base_urls:
#     r = requests.get(url)
#      soup = BeautifulSoup(r.text, 'html.parser')
#     print(soup)
#     images = soup.findAll('img', {'class': 'js-tile-hover-image is-hidden'})
#     for image in images:
#         print(image)

def get_male_product_pages():
    male_urls = [
        'https://www.tomford.co.uk/men/ready-to-wear/jackets/',
        'https://www.tomford.co.uk/men/ready-to-wear/evening/',
        'https://www.tomford.co.uk/men/ready-to-wear/jeans/',
        'https://www.tomford.co.uk/men/ready-to-wear/knitwear/',
        'https://www.tomford.co.uk/men/ready-to-wear/outerwear/',
        'https://www.tomford.co.uk/men/ready-to-wear/shirts/',
        'https://www.tomford.co.uk/men/ready-to-wear/suits/',
    ]
    
    for url in male_urls:
        get_product_pages_from_category('male', url)
        sleep(1)

def get_female_product_pages():
    female_urls = [
        'https://www.tomford.co.uk/women/ready-to-wear/dresses/',
        'https://www.tomford.co.uk/women/ready-to-wear/evening/',
        'https://www.tomford.co.uk/women/ready-to-wear/jackets/',
        'https://www.tomford.co.uk/women/ready-to-wear/knitwear/',
        'https://www.tomford.co.uk/women/ready-to-wear/pants-%26-shorts/',
        'https://www.tomford.co.uk/women/ready-to-wear/skirts/',
        'https://www.tomford.co.uk/women/ready-to-wear/tops/'
    ]
    
    for url in female_urls:
        get_product_pages_from_category('female', url)
        # break
        sleep(1)

def get_product_pages_from_category(gender, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    products = soup.findAll('li', {'class': 'grid-tile'})
    for product in products:
        # print(product.find('a')['href'])
        try:
            link = product.find('a')['href']
            print('image found, pushing into db')
            insert_product_into_db('tom ford', gender, url, link)
        except Exception as ex:
            print(ex)

def insert_product_into_db(brand_name, gender, category_url, product_page_url):
    SQL = """
        INSERT INTO fashion_product_page
            (brand_name, gender, category_url, product_page_url, created_at, updated_at)
        VALUES 
            (%s, %s, %s, %s, now(), now())
        ON CONFLICT DO NOTHING;
    """

    commit(SQL, [
        brand_name,
        gender,
        category_url,
        product_page_url
    ])

def insert_image_url_into_db(brand_name, gender, product_page_url, image_url, image_name):
    SQL = """
        INSERT INTO fashion_image_links
            (brand_name, gender, product_page_url, image_url, image_name, created_at, updated_at)
        VALUES
            (%s, %s, %s, %s, %s, now(), now())
        ON CONFLICT DO NOTHING;
    """

    commit(SQL, [
        brand_name,
        gender,
        product_page_url,
        image_url,
        image_name
    ])

def get_image_links():
    SQL = """
        SELECT * FROM fashion_product_page; 
    """

    records = fetch(SQL)
    print(len(records))

    for record in records:
        print(record['product_page_url'])
        image_url = extract_image_url_from_product_page(record['product_page_url'])
        if image_url:
            image_name = '{}_{}_{}'.format(record['brand_name'], record['gender'], record['id']).replace(' ', '_')
            print(image_url, image_name)
            insert_image_url_into_db(
                record['brand_name'],
                record['gender'],
                record['product_page_url'],
                image_url,
                image_name
            )

def extract_image_url_from_product_page(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text)
    images = soup.find('ul', {'id': 'thumbnails'}).findAll('li')
    for image in images:
        image_url = image.find('img')['src'].split('?')[0]
        # image ending in b is the one I am after
        if image_url.endswith('B'):
            return image_url

    return None

if __name__ == '__main__':
    # get_male_product_pages()
    # get_female_product_pages()
    get_image_links()