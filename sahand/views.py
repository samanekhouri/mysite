from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request,'sahand/index.html')

def about_view(request):
    return render(request,'sahand/About.html ')

def contact_view(request):
    return render(request,'sahand/Contact.html')