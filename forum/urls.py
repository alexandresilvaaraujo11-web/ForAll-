from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.lista_projetos, name='lista_projetos'),
     path('novo_projeto/', views.novo_projeto, name='novo_projeto'),
     path('deletar/<int:pk>/', views.delete_projeto, name='deletar_projeto'),
     
]

