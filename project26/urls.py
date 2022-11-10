"""project26 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('Cbv_string/',Cbv_string.as_view(),name='Cbv_string'),
    path('FBV_html/',FBV_html,name='FBV_html'),
    path('CBV_html/',CBV_html.as_view(),name='CBV_html'),
    path('FBV_djform/',FBV_djform,name='FBV_djform'),
    path('CBV_djform/',CBV_djform.as_view(),name='CBV_djform'),
    path('FBV_Mdform/',FBV_Mdform,name='FBV_Mdform'),
    path('CBV_Mdform/',CBV_Mdform.as_view(),name='CBV_Mdform'),
    path('CBV_TVhtml/',CBV_TVhtml.as_view(),name='CBV_TVhtml'),

]
