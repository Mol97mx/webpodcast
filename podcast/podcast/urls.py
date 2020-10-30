"""podcast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from nucleo import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('primeroA/',views.primeroA,name="Primero A"),
    path('primeroB/',views.primeroB,name="Primero B"),
    path('terceroA/',views.terceroA,name="Tercero A"),
    path('terceroB/',views.terceroB,name="Tercero B"),
    path('admin/', admin.site.urls),
]
