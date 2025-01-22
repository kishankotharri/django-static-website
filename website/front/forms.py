from django import forms    
from .models import ContactForm

class ContactFormClass(forms.ModelForm):    
    class Meta:
        model = ContactForm
        fields = ("__all__")