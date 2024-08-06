from django.db import models

class MetaData(models.Model):
    hashed_image_id = models.CharField(max_length=255, unique=True)
    publisher_id = models.CharField(max_length=255)
    published_date = models.DateField()
    liked_count = models.IntegerField()
    disliked_count = models.IntegerField()
