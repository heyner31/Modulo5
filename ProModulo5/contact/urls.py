from django.urls import path
from . import views

contact_urlpatterns = ([
    path('',views.contact, name='contact'),
    path('thanks/',views.thanks, name='thanks'),
], 'contact')