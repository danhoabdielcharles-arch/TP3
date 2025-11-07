# tp3/website/views.py
from django.shortcuts import render

def index(request):
    context = {
        'title': 'TP WEB L3 Info',
        'about': get_about()
    }
    return render(request, 'website/index.html', context)

def about(request):

    context = {
        'title': 'TP WEB L3 Info',
        'about': get_about()
    }
    return render(request, 'website/about.html', context)

def contact(request):
    return render(request, 'website/contact.html')

def services(request):
   return render(request, 'website/services.html')

def pricing(request):
   return render(request, 'website/pricing.html')

def servicesdetail(request):
    return render(request, 'website/servicesdetail.html')

def gallery (request):
    return render(request, 'website/gallery.html')

def blog (request):
    return render(request, 'website/blog.html')

def base (request):
    return render(request, 'website/base.html')

def singleblogpostleftsidebar(request):
    return render(request, 'website/singleblogpostleftsidebar.html')

def singleblogpostrightsidebar (request):
    return render(request, 'website/singleblogpostrightsidebar.html')

def singleblogpostwithoutsidebar (request):
    return render(request, 'website/singleblogpostwithoutsidebar.html')

#def (request):
#   return render(request, 'website/.html')

#def (request):
 #   return render(request, 'website/.html')









def get_about():
    data = {
        'section_title': 'Since 1998',
        'about_title': 'Making transportation fast and safe',
        'description': """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            lorem Ipsum has been the industry standard dummy text ever since 
            the when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book.
        """,
        'about_author': 'Toto Titi',
        'about_fonction': "Directeur General",
        'about_service':[
            {
                'img':'1.svg',
                'title':'Fast Deliver',
                'description':'Lorem Ipsum',
                'order':1,
            },
            {
                'img':'1.svg',
                'title':'100% Satifaction',
                'description':'Lorem Ipsum',
                'order':2,
            },
            {
                'img':'3.svg',
                'title':'24x7 Service',
                'description':'Lorem Ipsum',
                'order':3,
            },
        ]
    }
    return data

