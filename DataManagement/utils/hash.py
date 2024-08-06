import hashlib
import os

def hash_image(image):
    _, ext = os.path.splitext(image.name)
    image_name = f"{hashlib.md5(image.name.encode()).hexdigest()}{ext}"
    hashed_image_id = hashlib.md5(image_name.encode()).hexdigest()
    
    return image_name, hashed_image_id