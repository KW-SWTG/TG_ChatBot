from django.shortcuts import render
from chatbot.models import Msg
from django.shortcuts import redirect

def home(request):
    return render(request, "home.html")

def chatbot(request):
    rsChat = Msg.objects.all()
    return render(request, "chat_page.html",
                  {
                      'rsChat' : rsChat
                  })

def chat_insert(request):
    cnote = request.GET['note']
    if cnote != "":
        rows = Msg.objects.create(usr_msg = cnote,)
        return redirect('/chatbot')
    #else:
        #alert("내용을 입력해주세요")

def chat_delete(request):
   rows = Msg.objects.all()
   dele = rows.delete()
   return render(request, "chat_page.html", {
                      'rsChat' : dele
                  })