from django.http import HttpResponse
from django.shortcuts import render


def reverse(request):
    user_text = request.GET['username']
    reverse = user_text[::-1]
    return render(request,'reverse.html',{'word':reverse})

def home(request):
    return render(request, "home.html")