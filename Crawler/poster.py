import requests
import json
import os
from urllib.parse import urlparse


import requests
import json

def post_data(data):
    api_url = "http://172.21.0.5:8000/api/post/"
    check_url = f"{api_url}check/{data['hashed_image_id']}/"  # New URL for checking existing data
    headers = {
        "Content-Type": "application/json"
    }

    check_response = requests.get(check_url, headers=headers)
    
    if check_response.status_code == 200:
        print(f"Data with hashed_image_id {data['hashed_image_id']} already exists. Skipping.")
        return False 
    
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
    with open(save_path, 'wb') as file:
        file.write(response.content)
