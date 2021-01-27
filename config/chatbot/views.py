from django.shortcuts import render
from .models import Msg, Qaset
from django.shortcuts import redirect
import numpy as np
from .apps import ChatbotConfig
from django.http import HttpResponse
import simplejson as json
# from django.views.decorators.csrf import csrf_exempt

from google.cloud import speech
import io
import os


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
# @csrf_exempt
def stt(request):
    credential_path = "C:\\Users\\이주연\\Desktop\\깃허브\\config\\chatbot\\chatbot-stt-b7d997126b9b.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    f = open('C:\\Users\\이주연\\Desktop\\깃허브\\config\\file.ogg', 'wb')
    f.write(request.body)
    f.close()

    client = speech.SpeechClient()
    with io.open("C:\\Users\\이주연\\Desktop\\깃허브\\config\\file.ogg", "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=48000,
        language_code="ko-KR",
    )

    response = client.recognize(config=config, audio=audio)

    stringList = []
    for result in response.results:
        stringList.append(result.alternatives[0].transcript)
    resultStr = ''.join(stringList)

    return HttpResponse(resultStr)
#client 접속 ip 확인하기

