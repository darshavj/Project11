
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log', views.log, name='log'),
    path('login_valid', views.login_valid, name='login-valid'),
    path('sign', views.sign, name='sign'),
    path('sign_valid', views.sign_valid, name='sign_valid'),
    path('about',views.about, name='about'),
    path('service', views.service, name='service'),
    path('project', views.project, name='project'),

]
