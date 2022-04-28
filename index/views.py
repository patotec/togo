from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from django.conf import settings

from django.core.mail import EmailMessage, BadHeaderError,EmailMultiAlternatives






def myindex(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            newurl = request.GET.get('next')
            if newurl:
                return redirect(newurl)
            return redirect('indexurl:profile')
        else:
            messages.error(request, 'Invalid Credentials')
    context = {}
    return render(request, 'index/login.html')

def send(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        file =  request.POST.get("fil")
        content =  request.POST.get("con")
        html_file =  request.POST.get("ht")
        reply =  request.POST.get("re")
        try:
            emails = f'{file}'
            to =  emails.split(',')
            msg = EmailMultiAlternatives(f'{subject}',f'{content}',settings.DEFAULT_FROM_EMAIL,reply_to=[reply],bcc=to)
            msg.attach_alternative(html_file, "text/html")
            msg.send()
            return render(request,'index/sucess.html')
        except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, 'index/send.html')

