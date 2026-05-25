from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.lista_projetos, name='lista_projetos'),
    path('novo_projeto/', views.novo_projeto, name='novo_projeto'),
    path('projeto/<int:projeto_id>/deletar/', views.deletar_projeto, name='deletar_projeto'),
    path('projeto/<int:projeto_id>/chat/', views.chat_projeto, name='chat_projeto'), 
    path('projeto/<int:projeto_id>/editar/', views.update_projeto, name='update_projeto'),
    
    path('projeto/<int:projeto_id>/chat/', views.chat_projeto, name='chat_projeto'), 
]

