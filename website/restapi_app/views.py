from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from front.models import ContactForm
from front.serializers import ContactFormSerializer

# for API
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

import json

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_data(request):
    if request.method == 'GET':
        try:
            all_contacts = ContactForm.objects.all()
            serializer_data = ContactFormSerializer(all_contacts, many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except ContactForm.DoesNotExist:
                return JsonResponse({"error": "Contacts not found."}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_data_by_id(request, data_id):
    if request.method == 'GET':
        try:
            contact = ContactForm.objects.get(id=data_id)
            serializer_data = ContactFormSerializer(contact)
            return JsonResponse(serializer_data.data, safe=False)
        except ContactForm.DoesNotExist:
            return JsonResponse({"error": "Contact not found."}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_data(request):
    if request.method == 'POST':
        serializer_data = ContactFormSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data, safe=False)
        return JsonResponse({"error": "Somthing wrong."}, status=404)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
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
        
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_data_by_id(request, data_id):
    try:
        contact = ContactForm.objects.get(id=data_id)
        contact.delete()
        return JsonResponse({"message": "Records deleted."}, status=200)
    except ContactForm.DoesNotExist:
        return JsonResponse({"error": "Contact not found."}, status=404)
