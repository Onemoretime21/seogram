from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    ln = LatestNews.objects.all()
    context = {
        "qwe": ln
    }
    return render(request, template_name='seo/index.html', context=context)

def about(request):
    ln = LatestNews.objects.all()
    context = {
        "qwe": ln
    }
    return render(request, template_name='seo/about.html', context=context)

def service(request):
    ln = LatestNews.objects.all()
    context = {
        "qwe": ln
    }
    return render(request, template_name='seo/service.html', context=context)

def blog(request):
    ln = LatestNews.objects.all()
    context = {
        "qwe": ln
    }
    return render(request, template_name='seo/blog.html', context=context)

def contact(request):
    ln = LatestNews.objects.all()
    context = {
        "qwe": ln
    }
    return render(request, template_name='seo/contact.html', context=context)

def details(request):
    ln = LatestNews.objects.all()
    context = {
        "qwe": ln
    }
    return render(request, template_name='seo/blog-details.html', context=context)