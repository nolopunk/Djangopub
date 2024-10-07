# formulario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.guardar_contacto, name='formulario'),            # Existing URL for the form
    path('success/', views.guardar_contacto, name='success'),           # Existing URL for success page
    path('error/', views.guardar_contacto, name='error'),           # Existing URL for error page
]
