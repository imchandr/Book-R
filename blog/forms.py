
from urllib import request
from django import forms
from blog.models import Comment, Post

class PostSearchForm(forms.Form):
    query = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        '''another way to style form elements'''

        super().__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update({
            'placeHolder': 'Searching for post?',
            'class': '  w-full px-4 py-1 text-gray-800  focus:outline-none'
        })
    
class NewPostForm(forms.ModelForm):
    
    
    class Meta:
        model = Post
        fields = ('title','image', 'body', 'status')
        
        
    def __init__(self, *args, **kwargs):
        '''another way to style form elements'''

        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeHolder': 'Post title',
            'class': ' w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['image'].widget.attrs.update({
            'placeHolder': 'Post image',
            'class': 'w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['body'].widget.attrs.update({
            'placeHolder': 'Post contents',
            'class': ' w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['status'].widget.attrs.update({
            
            'placeHolder': 'Status',
            'class': ' w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
            
        
            
        def clean(self):
            cleaned_data = super(NewPostForm, self).clean()
            title = cleaned_data.get('title')
            
            # checks if post with same title exits
            post = Post.objects.filter(title=title)
            user = request.user
            temp_user = (user == post.author)
            if post and temp_user:
                raise forms.ValidationError('Duplicate post')
class SharePostForm(forms.Form):
    '''form for sharing posts by email'''
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(widget = forms.Textarea(attrs={'rows':5, 'cols':25}), required = False)

class CommentForm(forms.ModelForm):
    '''form for making comments on blog post'''
    
    class Meta:
        model = Comment
        fields = ('body',)
