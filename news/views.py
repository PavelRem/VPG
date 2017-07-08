from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate

from .models import NewsData, Aboutus, Reference, Team

def index(request):
#    news_data = NewsData.objects.order_by('-pub_date')
    return redirect('news')

def team(request):
#    news_data = NewsData.objects.order_by('-pub_date')
    return render(request, 'Our group.html',  {'team': Team.objects.all()})

def reference(request):
    reference_list = Reference.objects.all()
    paginator = Paginator(reference_list, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        references = paginator.page(page)
    except PageNotAnInteger:
        references = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        references = paginator.page(paginator.num_pages)
    return render(request, 'media_about.html', {'references': references })

def news(request):
    data = {
        'news': NewsData.objects.order_by("-pub_date")[:3].all(),
        'slides': NewsData.objects.filter(slider=True).order_by("-pub_date")[:3].all()
    }
    for x in data['news']:
        x.text = x.text[:130] + ' ...'


    for x in data['slides']:
        x.text = x.text[:130] + ' ...'

    return render(request, 'index.html',  data)

def fullread(request, id_news):
    return render(request, 'News.html',  {'news_detail': NewsData.objects.get(pk=id_news)})

def login(request):
    return render(request, 'login.html',  {})
