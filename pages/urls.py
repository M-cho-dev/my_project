from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('a1_index', views.a1_index, name='a1_index'),
    path('a2_tenant', views.a2_tenant, name='a2_tenant'),
    path('a3_properties', views.a3_properties, name='a3_properties'),
]
