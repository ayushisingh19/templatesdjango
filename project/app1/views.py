from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def page(request):
   return redirect ('https://www.instagram.com')
