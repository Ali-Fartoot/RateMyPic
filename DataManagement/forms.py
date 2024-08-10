from django import forms
from django.utils import timezone
from .models import MetaData

class MetaDataForm(forms.ModelForm):
    image = forms.ImageField(help_text="Upload an image")
    publisher_id = forms.CharField(max_length=255, help_text="Enter the publisher ID")
    published_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now().date(),
        required=False  # Allow the form to be submitted even if this field is empty
    )
    liked_count = forms.IntegerField(
        min_value=0,
        initial=0,
        widget=forms.HiddenInput(),  # Make this field hidden
        required=False  # Ensure this field is not required
    )
    disliked_count = forms.IntegerField(
        min_value=0,
        initial=0,
        widget=forms.HiddenInput(),  # Make this field hidden
        required=False  # Ensure this field is not required
    )

    class Meta:
        model = MetaData
        fields = ['image', 'publisher_id', 'published_date', 'liked_count', 'disliked_count']
