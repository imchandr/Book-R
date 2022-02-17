from django import forms
from order.models import Order
class OrderCreateForm(forms.ModelForm):
        
    class Meta:
        model = Order
        fields = ['name', 'email', 'street','city','state',
                  'zip' ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeHolder': 'First Name',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-400 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['email'].widget.attrs.update({
            'placeHolder': 'Email',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-400 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['street'].widget.attrs.update({
            'placeHolder': 'Street',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-400 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['city'].widget.attrs.update({
            'placeHolder': 'City',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-400 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['state'].widget.attrs.update({
            'placeHolder': 'State',
            'class': 'w-full px-2 py-2 text-md placeholder-gray-400 focus:outline-none border border-blue-400 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['zip'].widget.attrs.update({
            'placeHolder': 'Zip',
            'class': 'w-full px-2 py-2 text-md placeholder-gray-400 focus:outline-none border border-blue-400 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
