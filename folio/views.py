from django.shortcuts import render,redirect
from .models import Project,Skill,Personal_Information,Contact
from django.contrib import messages

# Create your views here.
def home(request):
    title = "JOSECK OGACHI"
    information = Personal_Information.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    # for info in information:
    #     information = info
    return render(request, 'home.html', {'title': title, 'projects': projects,
                                          'information': information, 'skills': skills})

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

    return redirect(home)
