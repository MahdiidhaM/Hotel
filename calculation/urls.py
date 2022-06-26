from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('',cal,name='cal'),
    path('Darvish/',Darvish,name='Darvish'),
    path('Almas2/',Almas2,name='Almas2'),
    path('Homa/',Homa,name='Homa'),
    path('Javad/',Javad,name='Javad'),
    path('Madineh-Al-Reza/',Madineh,name='Madineh-Al-Reza'),
    path('Sinoor/',Sinoor,name='Sinoor'),
    path('Ghasr/',Ghasr,name='hotelghasr'),
    path('Ghasr_Talaee/',Ghasr_Talaee,name='ghasrtalaee'),
    path('Homa_2/',Homa_2,name='Homa_2'),
    path('Pardisan/',Pardisan,name='Pardisan'),
    path('test/',test,name='test'),
]