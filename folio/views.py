from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

    return redirect(home)
