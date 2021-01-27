from django.shortcuts import render
from .models import Msg, Qaset
from django.shortcuts import redirect
import numpy as np
from .apps import ChatbotConfig
from django.http import HttpResponse
import simplejson as json


def home(request):
    return render(request, "home.html")

def chatbot(request):
    rsChat = Msg.objects.all()
    return render(request, "chat_pag.html",
                  {
                      'rsChat' : rsChat
                  })
def chat_insert(request):
    cnote = request.GET['note']
    if cnote != "":
        rows = Msg.objects.create(usr_msg = cnote,)
        # con_msg=ChatbotConfig.example(cnote);
        # print(con_msg);
        return redirect('/chatbot')
    else:
        return redirect('/chatbot')

def chat_delete(request):
   rows = Msg.objects.all()
   delete=rows.delete()
   return render(request, "chat_pag.html",)


def Prediction(x, y, z, a):
    result=""
    model = ChatbotConfig.models.predict(np.array([[x, y, z, a]]))

    if model[0]==1:
        result = "setosa"
    elif model[0]==2:
        result = "virginica"
    else:
        result = "nothing"

    return result

def model(request):
    x = int(request.POST['x']);

    result = Prediction(x, 4, 3, 1);
    context = {'result': result};
    return HttpResponse(json.dumps(context), content_type="application/json")

#client 접속 ip 확인하기

