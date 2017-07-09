from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator

from news.models import NewsData, Aboutus, Team, Reference, Partners

def activ(request):
    if request.method == "POST":
        obj = NewsData.objects.get(pk=int(request.POST.get('id', '')))
        obj.activity = False if obj.activity else True
        obj.save()
        print("activity ", obj.activity)
        return HttpResponse("true");
    return HttpResponse("false");

def monitor(request):
    if request.method == "POST":
        obj = NewsData.objects.get(pk=int(request.POST.get('id', '')))
        obj.monitoring = False if obj.monitoring else True
        obj.save()
        print("monitor ", obj.monitoring)
        return HttpResponse("true");
    return HttpResponse("false");

def slider(request):
    if request.method == "POST":
        obj = NewsData.objects.get(pk=int(request.POST.get('id', '')))
        obj.slider = False if obj.slider else True
        obj.save()
        print("slider ", obj.slider)
        return HttpResponse("true");
    return HttpResponse("false");

def news_update(request, id):
    return render(request, 'news_update.html',  {'news': NewsData.objects.get(pk=id)})

def news_update_save(request, id):
    if request.method == "POST":
        obj = NewsData.objects.get(pk=id)
        obj.title = request.POST.get('title', '')
        obj.text = request.POST.get('text', '')
        obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/news')
    return render(request, 'news_update.html',  {'news': NewsData.objects.all()})

def news_delete(request, id):
    print("id = ", id)
    obj = NewsData.objects.get(pk=id)
    obj.delete()
    return redirect('/admin/news')

def news_add(request):
    if request.method == "POST":
        obj = NewsData.objects.create()
        obj.title = request.POST.get('title', '')
        obj.text = request.POST.get('text', '')
        obj.img = request.FILES.get('photo', '')
        obj.activity = True if request.POST.get('activity', '') else False
        obj.monitoring =  True if request.POST.get('monitor', '') else False
        obj.slider =  True if request.POST.get('slider', '') else False
        obj.save()
        return redirect('/admin/news')
    return render(request, 'news_add.html',  {'news': NewsData.objects.all()})

def news(request):
    news_list = NewsData.objects.all().order_by('-pub_date')
    paginator = Paginator(news_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {'news': news })

def reference(request):
    reference_list = Reference.objects.all().order_by('-pub_date')
    paginator = Paginator(reference_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        references = paginator.page(page)
    except PageNotAnInteger:
        references = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        references = paginator.page(paginator.num_pages)
    return render(request, 'reference.html', {'references': references })

def reference_add(request):
    return render(request, 'ref_add.html',  {})


def reference_add_save(request):
    if request.method == "POST":
        obj = Reference.objects.create()
        obj.title = request.POST.get('title', '')
        obj.link = request.POST.get('link', '')
        obj.source = request.POST.get('source', '')
        obj.save()
        return redirect('/admin/reference')
    return render(request, 'reference.html',  {'references': Reference.objects.all()})

def reference_update(request, id):
    return render(request, 'ref_update.html',  {'ref': Reference.objects.get(pk=id)})

def reference_update_save(request, id):
    if request.method == "POST":
        obj = Reference.objects.get(pk=id)
        obj.title = request.POST.get('title', '')
        obj.link = request.POST.get('link', '')
        obj.source = request.POST.get('source', '')
        obj.save()
        return redirect('/admin/reference')
    return render(request, 'reference.html',  {'references': Reference.objects.all()})

def reference_delete(request, id):
    Reference.objects.get(pk=id).delete()
    return redirect('/admin/reference/')

def team(request):
    return render(request, 'team.html',  {'team': Team.objects.all()})

def team_add(request):
    if request.method == "POST":
        obj = Team.objects.create()
        obj.name = request.POST.get('name', '')
        obj.descrip = request.POST.get('descrip', '')
        obj.fb = request.POST.get('fb', '')
        obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/team/')

    return render(request, 'team_add.html',  {})

def team_change(request, id):
    if request.method == "POST":
        obj = Team.objects.get(pk=id)
        obj.name = request.POST.get('name', '')
        obj.descrip = request.POST.get('descrip', '')
        obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/team/')
    return render(request, 'team_change.html',  {'member': Team.objects.get(pk=id)})

def team_delete(request, id):
    Team.objects.get(pk=id).delete()
    return redirect('/admin/team/')

def about(request):
    try:
        return render(request, 'about.html',  {'info': Aboutus.objects.all()[0].text})
    except:
        return render(request, 'about.html',  {'info': ''})

def change_aboutus(request):
    if Aboutus.objects.all().count():
        obj = Aboutus.objects.all()[:1].get()
    else:
        obj = Aboutus.objects.create()
    obj.text = request.POST['text']
    obj.save()
    return redirect('/admin/about')


def partners(request):
    return render(request, 'partners.html',  {'partners': Partners.objects.all()})

def partners_add(request):
    return render(request, 'partners_add.html',  {})

def partners_add_save(request):
    if request.method == "POST":
        obj = Partners.objects.create()
        obj.name = request.POST.get('name', '')
        obj.descrip = request.POST.get('text', '')
        obj.link = request.POST.get('ref', '')
        obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/partners/')

    return render(request, 'partners.html',  {'partners': Partners.objects.all()})

def partners_update(request, id):
    return render(request, 'partner_update.html',  {'partner': Partners.objects.get(pk=id)})

def partners_update_save(request, id):
    if request.method == "POST":
        obj = Partners.objects.get(pk=id)
        obj.name = request.POST.get('name', '')
        obj.descrip = request.POST.get('text', '')
        obj.link = request.POST.get('ref', '')
        obj.img = request.FILES.get('photo', '')
        obj.save()
        return redirect('/admin/partners')
    return render(request, 'partners.html',  {'partners': Partners.objects.all()})

def partners_delete(request, id):
    Partners.objects.get(pk=id).delete()
    return redirect('/admin/partners/')
