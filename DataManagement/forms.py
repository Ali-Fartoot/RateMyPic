from django import forms
from django.utils import timezone
from .models import MetaData

class MetaDataForm(forms.ModelForm):
    image = forms.ImageField(help_text="Upload an image")
    publisher_id = forms.CharField(max_length=255, help_text="Enter the publisher ID")
    published_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now().date()
    )    
    liked_count = forms.IntegerField(min_value=0)
    disliked_count = forms.IntegerField(min_value=0)

    class Meta:
        model = MetaData
        fields = ['publisher_id', 'published_date', 'liked_count', 'disliked_count']
