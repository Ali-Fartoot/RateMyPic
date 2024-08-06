import requests
import json

def post_data(data):
    api_url = "http://172.21.0.5:8000/api/post/"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        print("Data posted successfully")
    else:
        print(f"Failed to post data: {response.status_code}")


        
def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url}")
    else:
        print(f"Failed to download {url}")
