from django import forms
from .models import Offer

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        
    def clean_recipients(self):
        data = self.cleaned_data['email']
        if "@union.edu" not in data:
            raise forms.ValidationError("Available only for the Union community. Please use your '@union.edu' email address.")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data
