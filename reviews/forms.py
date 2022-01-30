from django import forms
from reviews.models import Book

class AddReviewForm(forms.Form):
    
    review_content = forms.CharField(min_length=5, max_length=100,widget=forms.Textarea)
    rating = forms.IntegerField(max_value=5, min_value=1)
    
