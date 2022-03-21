from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Website,Url




def createUrl(req):
    if req.method == "post":
        full_url = req.POST.get('full_url')
        obj = Url.create(full_url)
        return  render(req, 'URLshortenerapp/index.html', {
            'full_url' : obj.full_url,
            'short_url' : req.get_host() + '/'+obj.short_url
        })
    return render(req, 'URLshortenerapp/index.html')

def routeToURL(req, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(createUrl)

def homeView(request):
    name = "Welcome to"

    obj = Website.objects.get(id=1)
    context = {
        'name': name,
        'obj': obj,

    }

    return render(request, 'URLshortenerapp/home.html', context)





