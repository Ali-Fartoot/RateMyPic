import os
import requests
from bs4 import BeautifulSoup
import re
import poster
from datetime import datetime
import pytz
from datetime import date, datetime
from urllib.parse import urlparse


url = "https://www.waifu.im/search/?included_tags=waifu"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
script_tags = soup.find_all()
img_urls = re.findall(r'https://cdn\.waifu\.im/\d+\.(?:jpg|jpeg|png)', str(script_tags))



for img_url in img_urls:
    filename = os.path.basename(urlparse(img_url).path)

    data = {
        "hashed_image_id": filename,
        "publisher_id": "Crawler",
        "published_date": date.today().isoformat(),
        "liked_count": 0,
        "disliked_count": 0
    }

    response = poster.post_data(data)
    if response: 
        poster.download_image(img_url, os.path.join(os.getcwd(), "cache_images")
)