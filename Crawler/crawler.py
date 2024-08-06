import os
import requests
from bs4 import BeautifulSoup
import re
import poster
from datetime import datetime
import pytz

url = "https://www.waifu.im/search/?included_tags=waifu"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
script_tags = soup.find_all()
img_urls = re.findall(r'https://cdn\.waifu\.im/\d+\.(?:jpg|jpeg|png)', str(script_tags))


save_dir = "cache_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


for img_url in img_urls:
    data = {
        "hashed_image_id": img_url,
        "publisher_id": "Crawler",
        "published_date": datetime.now(pytz.timezone('Asia/Tehran')).isoformat(),
        "liked_count": 0,
        "disliked_count": 0
    }
    
    save_path = "../Images"
    poster.download_image(img_url, save_path)
    poster.post_data(data)