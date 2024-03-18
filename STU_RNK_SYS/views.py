from django.shortcuts import render,redirect
from django.http import request

def home(request):
    return render(request,'home.html')

