from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chatbot', views.chatbot, name="chatbot"),
    path('chat_insert', views.chat_insert, name="chat_insert"),
    path('chat_delete', views.chat_delete, name="chat_delete"),

]