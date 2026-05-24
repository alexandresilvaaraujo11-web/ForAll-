from django.urls import path, include
from .views import chat
app_name = 'chat'

urlpatterns = [
    path('chat/', chat, name='chat'),
]
