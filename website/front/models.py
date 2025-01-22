from django.db import models

# Create your models here.
class ContactForm(models.Model):
    PROFILE_OPTIONS = {
        "Profile": "Profile",
        "Dashboard": "Dashboard",
        "Services": "Menu (Quotation, Installtion, Service, Other)",
        "Products": "Product List",
        "Invoice": "Invoice History",
        "Other": "Other than Above",
    }

    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    profile = models.CharField(max_length=50, choices=PROFILE_OPTIONS)
    file = models.FileField(upload_to='uploads/front/', blank=True, null=True)
    message = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.full_name + " : " + self.email