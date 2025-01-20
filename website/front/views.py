from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm
from .models import ContactForm
from .serializers import ContactFormSerializer

# Create your views here.
def index(request):
    return render(request, "front/index.html")

def faqs(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return render(request, "front/faqs.html", {'contact_form':contact_form, 'contact_form_error': False, 'contact_form_message': 'Successfully submitted.'})
        else:
            return render(request, "front/faqs.html", {'contact_form':contact_form, 'contact_form_error': True, 'contact_form_message': contact_form.errors})
    else:
        contact_form = ContactForm()
        return render(request, "front/faqs.html", {'contact_form':contact_form, 'contact_form_error': False, 'contact_form_message': ''})

def contacts(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return render(request, "front/contacts.html", {'contact_form':contact_form, 'contact_form_error': False, 'contact_form_message': 'Successfully submitted.'})
        else:
            return render(request, "front/contacts.html", {'contact_form':contact_form, 'contact_form_error': True, 'contact_form_message': contact_form.errors})
    else:
        contact_form = ContactForm()
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
