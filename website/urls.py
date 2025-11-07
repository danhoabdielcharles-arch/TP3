from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='root'),
    path('l3info', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),



    path('services.html', views.services, name='services'),
    path('pricing.html', views.pricing, name='pricing'),
    path('servicesdetail.html', views.servicesdetail, name='servicesdetail'),
    path('gallery.html', views.gallery, name='gallery'),
    path('blog.html', views.blog, name='blog'),
    path('base.html', views.base, name='base'),
    path('singleblogpostleftsidebar.html', views.singleblogpostleftsidebar, name='singleblogpostleftsidebar'),
    path('singleblogpostrightsidebar.html', views.singleblogpostrightsidebar, name='singleblogpostrightsidebar'),
    path('singleblogpostwithoutsidebar.html', views.singleblogpostwithoutsidebar, name='singleblogpostwithoutsidebar'),

    

]