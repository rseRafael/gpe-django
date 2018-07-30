from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.uploadfile),
    path('render/<str:msg>/', views.test),
    path('formulario/', views.formulario)
]