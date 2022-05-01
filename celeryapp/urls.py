"""celeryapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from calculation.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Snap/',Snap),
    path('Ali_task/',Snap_task),
    path('price/',price),
    path('Darvish/',Darvish,name='Darvish'),
    path('Almas/',Almas,name='Almas'),
    path('Homa/',Homa,name='Homa'),
    path('Javad/',Javad,name='Javad'),
    path('Ghasr/',Ghasr,name='Ghasr'),
]
