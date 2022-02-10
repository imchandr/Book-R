from django import forms
from reviews.models import Book, Review

class ReviewForm(forms.ModelForm):
    '''form for addig revies on book'''
    
    class Meta:
        model = Review
        fields = ('content','rating')
        
    def __init__(self, *args, **kwargs):
        '''another way to style form elements'''

        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'placeHolder': 'Add Review',
            'class': 'bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-20 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white'
        }) 
        self.fields['rating'].widget.attrs.update({
            'placeHolder': 'Add Review',
            'class': 'rounded border border-gray-400 leading-normal resize-none w-full  py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white'
        })  
