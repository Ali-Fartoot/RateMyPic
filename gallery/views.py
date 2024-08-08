import os
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from DataManagement.models import MetaData
from django.conf import settings
from PIL import Image
import io
import base64
from django.db.models import F

def image_gallery(request):
    # Get the sorting parameter from the request
    sort_by = request.GET.get('sort', 'likes')  # Default sort by likes

    # Apply sorting based on the parameter
    if sort_by == 'likes':
        all_images = MetaData.objects.all().order_by('-liked_count')
    elif sort_by == 'average_rating':
        all_images = MetaData.objects.annotate(
            avg_rating=F('liked_count') - F('disliked_count')
        ).order_by('-avg_rating')
    elif sort_by == 'date':
        all_images = MetaData.objects.all().order_by('-published_date')
    else:
        # Default to sorting by likes if an invalid parameter is provided
        all_images = MetaData.objects.all().order_by('-liked_count')

    paginator = Paginator(all_images, 16)  # Show 16 images per page
    
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)
    
    image_data = []
    for image in page_obj:
        image_data.append({
            'hashed_image_id': image.hashed_image_id,
            'publisher_id': image.publisher_id,
            'published_date': image.published_date,
            'liked_count': image.liked_count,
            'disliked_count': image.disliked_count,
            'average_rating': image.liked_count - image.disliked_count  # Calculate average rating
        })
    
    context = {
        'image_data': image_data,
        'page_obj': page_obj,
        'MEDIA_URL': settings.MEDIA_URL,
        'current_sort': sort_by  # Pass the current sorting option to the template
    }
    
    return render(request, 'gallery.html', context)
