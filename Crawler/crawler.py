import os
import requests
from bs4 import BeautifulSoup
import re
import poster
from datetime import datetime
import pytz
from datetime import date, datetime
from urllib.parse import urlparse
from poster import download_image, post_data

url = "https://www.waifu.im/search/?included_tags=waifu"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
script_tags = soup.find_all()
img_urls = re.findall(r'https://cdn\.waifu\.im/\d+\.(?:jpg|jpeg|png)', str(script_tags))


save_path = os.path.join(os.getcwd(), "cache_images")
for img_url in img_urls:
    filename = os.path.basename(urlparse(img_url).path)

    data = {
        "hashed_image_id": filename,
        "publisher_id": "Crawler",
        "published_date": date.today().isoformat(),
        "liked_count": 0,
        "disliked_count": 0
    }
    if download_image(img_url, save_path):
        print("Image downloaded successfully")
        if post_data(data):
            print("Data posted successfully")
        else:
            print("Failed to post data")
    else:
        print("Failed to download image")