from django import forms
#from .models import Report
from .models import Post, Comment, IncidentReport
'''
class ReportForm(forms.ModelForm):
    class Meta:
        #model = Report
        fields = ['title', 'description', 'latitude', 'longitude']
'''
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  

        # for custom styling
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post...'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a comment...'}),
        }
class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['title', 'description', 'location']
