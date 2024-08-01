from django.db import models

class MetaData(models.Model):

    hashed_image_id = models.CharField()
    publisher_id = models.CharField()
    published_date = models.DateField()
    liked_count = models.IntegerField()
    disliked_count = models.IntegerField()


# MetaData(hashed_image_id="a21312123asdas", publisher_id="1easd3h76lk8", published_date=ti
# mezone.now(), liked_count=321, disliked_count=31).save() 

# from django.utils import timezone  
# from DataManagement.models import MetaData