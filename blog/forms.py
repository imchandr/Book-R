from django import forms
from blog.models import Comment

class EmailPostForm(forms.Form):
    '''form for sharing posts by email'''
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(widget = forms.Textarea(attrs={'rows':5, 'cols':25}), required = False)

class NewCommentForm(forms.Form):
    '''form for making comments on blog post'''
    
    class Meta:
        model = Comment
        fields = ('name','body')
