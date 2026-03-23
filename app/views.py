from django.shortcuts import render

def home(request):
    return render(request, 'home_page.html')

def menu(request):
    return render(request, 'menu.html')

