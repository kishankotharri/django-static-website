from django.contrib import admin
from .models import ContactForm

# Register your models here.
@admin.register(ContactForm) 
class ContactFormAdmin(admin.ModelAdmin): 
    list_display = ("full_name", "email")