from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def home(request):
    # return HttpResponse("This is Home Page")
    context = {
        'name':'Nitesh Kumar Jha',
        'topic':'Django'
    }
    return render(request,'home.html',context)

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phone = request.POST.get('phone')

        contact = Contact(name = name,email = email, desc = desc, phone = phone, date = datetime.today())
        contact.save()
        messages.success(request,'Form Submitted Successfully !')
    return render(request,'contact.html')