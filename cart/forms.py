from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,4)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int, initial='1')
    quantity.widget.attrs.update({
        
        'class': " inline form-select  block w-18 px-5 py-2 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out mr-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
    })
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)