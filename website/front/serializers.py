from rest_framework import serializers
from .models import ContactForm

# class ContactFormSerializer(serializers.Serializer):
#     full_name = serializers.CharField(max_length=100)
#     email = serializers.CharField(max_length=50)
#     profile = serializers.CharField(max_length=50)

class ContactFormSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ContactForm
        fields = ("__all__")