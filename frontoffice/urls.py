from os import name

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('', views.login, name="login"),
    path(r'register/', views.register, name="Reg"),
    path(r'index/', views.index, name="ind"),
    path('addMateriel/',views.updateMateriel, name='addMateriel'),
    path('Materiels/',views.getMateriels, name='Materiels'),
    path(r'deleteMateriel/(?P<id>.+)',views.deleteMat, name='deleteMateriel'),
    path('updateMateriel/(?P<id>.+)', views.updateMateriel, name='updateMateriel')
]