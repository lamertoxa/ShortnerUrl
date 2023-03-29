from django.shortcuts import render, redirect

from django.contrib import auth



def home(request):
    if request.method == 'POST':
        auth.logout(request)
    return render(request, 'index.html')

