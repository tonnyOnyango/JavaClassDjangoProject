from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def services(request):
    return render(request, 'services.html')

def news(request):
    return render(request, 'news.html')

def jobs(request):
    return render(request, 'jobs.html')