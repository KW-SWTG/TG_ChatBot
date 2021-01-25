from django.shortcuts import render
from .models import Msg
from django.shortcuts import redirect
import numpy as np
from .apps import ChatbotConfig
from django.http import HttpResponse
import json

def home(request):
    return render(request, "home.html")

def chatbot(request):
    rsChat = Msg.objects.all()
    # ChatbotConfig.example();
    # if rsChat.note !="": 비어있으면 아무것도 불러오지망
    return render(request, "chat_page.html",
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
   return render(request, "chat_page.html",)


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

    x = int(request.GET['x'])
    y = int(request.GET['y'])
    z = int(request.GET['z'])
    a = int(request.GET['a'])

    result = Prediction(x, y, z, a)

    context={ 'result': result }
    return HttpResponse(json.dumps(context), content_type="application/json")
    #return render(request, 'chat_page.html', {'result': result})
#입력하면 출력하기 chat_page에다가 string 전달
# def chat_update(request):
#
# class call_model(APIView):
#
#     def ??:
#     params=request.?get('뭘 불러와>')
#     response = ChatbotConfig.predictor.predict()
#     return response;
#client 접속 ip 확인하기

