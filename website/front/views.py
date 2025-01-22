from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import ContactFormClass
from .models import ContactForm
from .serializers import ContactFormSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

import json

# Create your views here.
def index(request):
    return render(request, "front/index.html")

def faqs(request):
    if request.method == "POST":
        contact_form = ContactFormClass(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return render(request, "front/faqs.html", {'contact_form':contact_form, 'contact_form_error': False, 'contact_form_message': 'Successfully submitted.'})
        else:
            return render(request, "front/faqs.html", {'contact_form':contact_form, 'contact_form_error': True, 'contact_form_message': contact_form.errors})
    else:
        contact_form = ContactFormClass()
        return render(request, "front/faqs.html", {'contact_form':contact_form, 'contact_form_error': False, 'contact_form_message': ''})

def contacts(request):
    if request.method == "POST":
        contact_form = ContactFormClass(request.POST, request.FILES)
        if contact_form.is_valid():
            contact_form.save()
            return render(request, "front/contacts.html", {'contact_form':contact_form, 'contact_form_error': False, 'contact_form_message': 'Successfully submitted.'})
        else:
            return render(request, "front/contacts.html", {'contact_form':contact_form, 'contact_form_error': True, 'contact_form_message': contact_form.errors})
    else:
        contact_form = ContactFormClass()
        return render(request, "front/contacts.html", {'contact_form':contact_form, 'contact_form_error': False, 'contact_form_message': ''})

def career(request):
    return render(request, "front/career.html")

def privacy_policy(request):
    return render(request, "front/privacy-policy.html")

def terms_conditions(request):
    return render(request, "front/terms-conditions.html")

def cookie_policy(request):
    return render(request, "front/cookie-policy.html")

def get_data(request):
    if request.method == 'GET':
        try:
            all_contacts = ContactForm.objects.all()
            serializer_data = ContactFormSerializer(all_contacts, many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except ContactForm.DoesNotExist:
                return JsonResponse({"error": "Contacts not found."}, status=404)
    
def get_data_by_id(request, data_id):
    if request.method == 'GET':
        try:
            contact = ContactForm.objects.get(id=data_id)
            serializer_data = ContactFormSerializer(contact)
            return JsonResponse(serializer_data.data, safe=False)
        except ContactForm.DoesNotExist:
            return JsonResponse({"error": "Contact not found."}, status=404)

@csrf_exempt
@api_view(['POST'])
def add_data(request):
    if request.method == 'POST':
        serializer_data = ContactFormSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data, safe=False)
        return JsonResponse({"error": "Somthing wrong."}, status=404)

@csrf_exempt
@api_view(['PUT'])
def update_data_by_id(request, data_id):
    if request.method == 'PUT':
        try:
            contact = ContactForm.objects.get(id=data_id)
            serializer_data = ContactFormSerializer(contact, data=request.data, partial=True)
            
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse(serializer_data.data, safe=False, status=200)
            else:
                return JsonResponse(serializer_data.errors, status=400)
        except ContactForm.DoesNotExist:
            return JsonResponse({"error": "Contact not found."}, status=404)
        
@csrf_exempt
def delete_data_by_id(request, data_id):
    if request.method == 'DELETE':
        try:
            contact = ContactForm.objects.get(id=data_id)
            contact.delete()
            return JsonResponse({"message": "Records deleted."}, status=200)
        except ContactForm.DoesNotExist:
            return JsonResponse({"error": "Contact not found."}, status=404)
