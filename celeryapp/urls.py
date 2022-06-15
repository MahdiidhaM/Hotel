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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('Madineh-Al-Reza/',Madineh,name='Madineh-Al-Reza'),
    path('Ali_task/',Eghamat_task),
    # path('price/',price),
    path('Darvish/',Darvish,name='Darvish'),
    path('Almas2/',Almas2,name='Almas2'),
    path('Homa/',Homa,name='Homa'),
    path('Javad/',Javad,name='Javad'),
    path('cal/',cal,name='cal'),
    path('SignUp/',sign_up,name='register'),
    path('aj/',aj,name='aj'),
    path('Sinoor/',Sinoor,name='Sinoor'),
    path('Ghasr/',Ghasr,name='hotelghasr'),
    path('Ghasr_Talaee/',Ghasr_Talaee,name='ghasrtalaee'),
    path('Homa_2/',Homa_2,name='Homa_2'),
    path('Pardisan/',Pardisan,name='Pardisan'),

    
    # path('main/',main,name='main'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)