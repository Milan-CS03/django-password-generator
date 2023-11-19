from django.shortcuts import render
import random

# Create your views here.
from django.http import  HttpResponse

def home(request):
    req = request
    return  render(request, 'generator/home.html', {'req': req})

def about(request):
    return  render(request, 'generator/about.html')
def password(request):
    #thepassword = 'testpass'
    chars = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('uppercase'):
        chars.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special'):
        chars.extend(list("!@#$%^&*()"))
    if request.GET.get('number'):
        chars.extend(list("1234567890"))
    lenght = int(request.GET.get('length', 12))

    thepassword = ""
    for x in range(lenght):
        thepassword += random.choice(chars)

    return  render(request, 'generator/password.html', {'password': thepassword})