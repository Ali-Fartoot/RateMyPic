import os
from urllib.parse import urlparse
import requests
import json

def post_data(data):
    api_url = "http://192.168.0.5:8000/api/post/"
    check_url = f"{api_url}check/{data['hashed_image_id']}/"
    headers = {
        "Content-Type": "application/json"
    }

    check_response = requests.get(check_url)
    if check_response.status_code == 200:
        print("Data already exists in the database. Skipping upload.")
        return True

    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print("Data posted successfully")
        return True
    else:
        print(f"Failed to post data: {response.status_code}")
        return False

def download_image(url, save_path):
    filename = os.path.basename(urlparse(url).path)
    save_path = os.path.join(save_path, filename)
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False
