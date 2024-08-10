import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .forms import MetaDataForm
from .utils.hash import hash_image
from django.urls import reverse
from django.db import IntegrityError

def upload_image(request):
    if request.method == 'POST':
        form = MetaDataForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES.get('image')
            
            if image:
                image_name, hashed_image_id = hash_image(image)
                image_path = os.path.join(image_name)
                print(image_path)
                path = default_storage.save(image_path, ContentFile(image.read()))
                
                metadata = form.save(commit=False)
                metadata.hashed_image_id = image_name

                try:
                    metadata.save()
                    return redirect('/upload/success/')
                except IntegrityError:
                    form.add_error('image', 'An image with this hash already exists in the database.')
            else:
                form.add_error('image', 'No image uploaded')
        else:
            print("Form errors:", form.errors)
    else:
        form = MetaDataForm()
    
    return render(request, 'upload.html', {'form': form})


def upload_success(request):
    home_url = reverse('home')
    return render(request, 'success.html', {'home_url': home_url})
