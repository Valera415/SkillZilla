from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('stack/', stack, name='stack'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),

]

