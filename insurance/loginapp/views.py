from django.shortcuts import render
from django.http import HttpResponse
from loginapp import forms

# Create your views here.

def login(request):
    form = forms.Insurance_form()
    return render(request, 'loginapp/login_page.html',{'form' :form})
