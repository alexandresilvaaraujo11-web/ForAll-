from django.urls import path, include
from .views import chat_sala
app_name = 'chat'

urlpatterns = [
    path('sala/<int:sala_id>/', chat_sala, name='chat_sala'),
]
