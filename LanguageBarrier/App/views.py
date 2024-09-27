from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def map(request):
    return render(request, 'map.html')

def blog(request):
    return render(request,'blog.html')