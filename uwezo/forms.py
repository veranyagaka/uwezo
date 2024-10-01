# geotagging/forms.py
from django import forms
#from .models import Report
from .models import Post
class ReportForm(forms.ModelForm):
    class Meta:
        #model = Report
        fields = ['title', 'description', 'latitude', 'longitude']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  # Only include the content field in the form

        # for custom styling
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post...'}),
        }