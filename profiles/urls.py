from django.urls import path
from .views import register, login , logout_profile #, new_entrada, update_entrada, delete_entrada 
app_name = 'profile' 

urlpatterns = [ 
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout_profile', logout_profile, name='logout_profile'),
    #path('list_entrada/', list_entrada, name='list_entrada'), 
    #path('new_entrada/', new_entrada, name='new_entrada'), 
    #path('update_entrada/<int:pk>/', update_entrada, name='update_entrada'), 
    #path('delete_entrada/<int:pk>/', delete_entrada, name='delete_entrada'), 
]