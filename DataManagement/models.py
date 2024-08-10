from django.db import models
from django.utils import timezone

class MetaData(models.Model):
    hashed_image_id = models.CharField(max_length=255, unique=True)
    publisher_id = models.CharField(max_length=255)
    published_date = models.DateField(default=timezone.now().date())
    liked_count = models.IntegerField(default=0)
    disliked_count = models.IntegerField(default=0) 
