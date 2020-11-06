from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def chatbot(request):
    return render(request, "chat_page.html",)