from django.shortcuts import render
from .forms import ContactFormClass

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

