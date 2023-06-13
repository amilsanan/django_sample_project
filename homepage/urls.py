from django.urls import path
from . import views
# from django.conf import settings



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('form/', views.form, name='form'),
    
    
     path('form/', views.form, name='form'),
    
]