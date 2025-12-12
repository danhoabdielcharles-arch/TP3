# tp3/website/views.py
from django.shortcuts import render # type: ignore
from .models import slider, banner3, About, banner, Services, ServiceHeader, FeatureHeader


def index(request):
    feature_header = FeatureHeader.objects.filter(page='index').first()
    feature_items = feature_header.items.all() if feature_header else []

    context = {
        'title': 'index',

        # bannière
         'banners': banner.objects.filter(page='index'),

        # slider
        'sliders': slider.objects.all(),

        # about
        'about': About.objects.filter(page='index').first(),

        # services
        'services': Services.objects.filter(actif=True).order_by('ordre'),
        'service_header': ServiceHeader.objects.filter(page='index').first(),

         'feature_header': feature_header, 
         'feature_items': feature_items,
 
    }

    return render(request, 'website/index.html', context)


def about(request):
    banners = banner.objects.filter(page='about')
    about_data = About.objects.filter(page='about').first()

    context = {
        'title': 'about',
        'about': about_data,
        'banners': banners,
    }
    return render(request, 'website/about.html', context)

def contact(request):
    banners = banner.objects.filter(page='contact')
    return render(request, 'website/contact.html', {'banners': banners})

def services(request):
    banners = banner.objects.filter(page='services')
    about_data = About.objects.filter(page='services').first()
    
    feature_header = FeatureHeader.objects.filter(page='services').first()
    feature_items = feature_header.items.all() if feature_header else []
    
    service_header = ServiceHeader.objects.filter(page='services').first()
    services_list = Services.objects.filter(actif=True).order_by('ordre')
    
    context = {
        'about': about_data,
        'banners': banners,
        'services': services_list,
        'service_header': service_header,
        'feature_header': feature_header,
        'feature_items': feature_items,
    }
    
    return render(request, 'website/our-services.html', context)


def pricing(request):
    banners = banner.objects.filter(page='pricing')
    return render(request, 'website/pricing.html', {'banners': banners})

def servicesdetail(request):
    banners = banner.objects.filter(page='servicesdetail')
    return render(request, 'website/servicesdetail.html', {'banners': banners})

def gallery(request):
    banners = banner.objects.filter(page='gallery')
    return render(request, 'website/gallery.html', {'banners': banners})

def blog(request):
    banners = banner.objects.filter(page='blog')
    return render(request, 'website/blog.html', {'banners': banners})

def base(request):
    banners = banner.objects.filter(page='base')
    return render(request, 'website/base.html', {'banners': banners})

def team(request):
    banners = banner.objects.filter(page='team')
    return render(request, 'website/team.html', {'banners': banners})

def singleblogpostleftsidebar(request):
    banners = banner.objects.filter(page='singleblogpostleftsidebar')
    banners3_item = banner3.objects.filter(page='singleblogpostleftsidebar'). first()
    return render(request, 'website/singleblogpostleftsidebar.html', {'banners': banners, 'banners3_item': banners3_item})

def singleblogpostrightsidebar(request):
    banners = banner.objects.filter(page='singleblogpostrightsidebar')
    banners3_item = banner3.objects.filter(page='singleblogpostrightsidebar'). first()
    return render(request, 'website/single-blog-post-rightsidebar.html', {'banners': banners, 'banners3_item': banners3_item})

def singleblogpostwithoutsidebar(request):
    banners = banner.objects.filter(page='singleblogpostwithoutsidebar')
    banners3_item = banner3.objects.filter(page='singleblogpostwithoutsidebar'). first()
    return render(request, 'website/singleblogpostwithoutsidebar.html', {'banners': banners, 'banners3_item': banners3_item})




