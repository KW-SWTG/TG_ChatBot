from django.shortcuts import render
from django.shortcuts import redirect
import numpy as np
from .apps import ChatbotConfig
from django.http import HttpResponse
import simplejson as json
import re
import operator
from django.views.decorators.csrf import csrf_exempt
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from google.cloud import speech
from google.auth.exceptions import DefaultCredentialsError
import logging
import io
import os
from konlpy.tag import Twitter
import pandas as pd
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver


komoran = ChatbotConfig.komoran
f_model = ChatbotConfig.fmodel
twitter = Twitter()
b_model = ChatbotConfig.bmodel
ktok = ChatbotConfig.btokenizer
vectorzier_keys = ChatbotConfig.load_vectorlizer()


def home(request):
    return render(request, "home.html")


def chatbot(request):
    return render(request, "chat_pag.html",
                  {
                      'rsChat': "some"
                  })


def FCmatching(ip):
    category = ChatbotConfig.load_cate()
    p_cate = c_similarity(ip, f_model, category)
    # print(max(p_cate.items(), key=operator.itemgetter(1))[0])
    return str(max(p_cate.items(), key=operator.itemgetter(1))[0])


def SCmatching(f_keword, ip):
    features = vectorzier_keys[f_keword]['vec'].get_feature_names()
    srch = [t for t in hyungextrac(ip) if t in features]

    srch_dtm = np.asarray(vectorzier_keys[f_keword]['X'].toarray())[:, [
        vectorzier_keys[f_keword]['vec'].vocabulary_.get(i) for i in srch
    ]]
    score = srch_dtm.sum(axis=1)

    # max score
    print('max score : ', max(score))
    if max(score) < 0.54:
        return {"score": 0, "phrase": ""}

    return {"score": 1, "phrase": vectorzier_keys[f_keword]['raw'][np.argmax(score)]}


def tokenizer(raw, pos=["Noun", "Alpha", "Verb", "Number"], stopword=[]):
    return [
        word for word, tag in twitter.pos(
            raw,
            norm=True,
            stem=True
        )
        if len(word) > 1 and tag in pos and word not in stopword
    ]


def hyungextrac(text):
    temp = text
    if "샵" in temp:
        temp, a = re.subn('샵', '숍', temp)
    if "1회용품" in temp:
        temp, a = re.subn('1회', '일회', temp)
    temp = temp.replace("\n", " ")
    pos = komoran.pos(temp)
    morph = []
    for i in pos:
        if i[0] == "펜":
            morph.append("펜션")
            continue
        if i[0] == "션":
            continue
        if i[1] == "NNG" or i[1] == "NNP" or i[1] == "SL":
            morph.append(i[0])

    return morph
# 형태소 추출기 들어온 문장 등에서 사용하기 위해


def hybrida(ip):
    adic = ChatbotConfig.hyapi(ip)

    return adic


def c_similarity(Question, model, catelst):
    moon = hyungextrac(Question)
    dislst = {}

    simmat = []
    for i in moon:
        subsimmat = []
        for t in moon:
            subsimmat.append(model.similarity(i, t))
        simmat.append(subsimmat)
    simmat = np.array(simmat)
    glst = simmat.sum(axis=1)

    for i in catelst:
        hcate = hyungextrac(i)
        dislst[i] = 0
        for w in hcate:
            sc = 0
            for t in range(len(moon)):
                simsc = model.similarity(w, moon[t])
                simsc *= glst[t]
                sc += simsc
            dislst[i] += sc
        dislst[i] = dislst[i]/len(hcate)

    return dislst


def mrc(ip, para):
    ttemp = ChatbotConfig.mrc2api(ip, para)
    return ttemp


def Sear(sinput):
    baseUrl = 'https://www.google.com/search?q='
    plusUrl = sinput
    url = baseUrl + quote_plus(plusUrl)

    #driver = webdriver.Chrome(executable_path='C://wdb/친구6edriver.exe')
    driver = webdriver.Chrome(
        executable_path="C://Users//jeewo//Downloads//chromedriver_win32//chromedriver.exe")
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html)
    n1 = soup.select('.SzZmKb')
    n2 = soup.select('.SPZz6b')
    n3 = soup.select('.nawv0d')
    n4 = soup.select('.w7Dbne')
    result = ''
    if len(n1) > 0:
        try:
            result = n1[0].select_one('.FLP8od').text
        except:
            try:
                result = n2[0].select_one('.wwUB2c').text
            except:
                result = "결과 출력 할 수 없습니다."
    elif len(n2) > 0:
        try:
            result = n2[0].select_one('.wwUB2c').text
        except:
            result = "결과 출력 할 수 없습니다."
    elif len(n3) > 0:
        try:
            state_info = n3[0].select_one('.VQF4g').text
            degree = n3[0].select_one('.TylWce').span.text
            result = state_info + " "+degree+"'C"
        except:
            result = "결과 출력 할 수 없습니다."
    elif len(n4) > 0:
        try:
            for i in n4:
                result += i.select_one('.dbg0pd').text + "\n"
        except:
            print("결과 출력 할 수 없습니다.")
    else:
        result = "결과 출력 할 수 없습니다."

    driver.close()
    return result


def model(request):
    inputphrase = str(request.POST['x'])
    morphset = hyungextrac(inputphrase)
    f_keword = FCmatching(inputphrase)
    s_mdict = SCmatching(f_keword, inputphrase)
    print(s_mdict)

    if s_mdict['score'] == 1:
        result = ChatbotConfig.answering(
            inputphrase, s_mdict['phrase'], b_model, ktok)
        if result == "":
            result = hybrida(inputphrase)
    else:
        result = hybrida(inputphrase)

    context = {'result': result}
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def stt(request):
    credential_path = '..//sa-spoiler-4897b3e764af.json'
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

    f = open("chatbot/file.ogg", 'wb')
    f.write(request.body)
    f.close()
    with io.open("chatbot/file.ogg", "rb") as audio_file:
        content = audio_file.read()

    try:
        client = speech.SpeechClient()
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

    except DefaultCredentialsError:
        logging.warning('DefaultCredentaials error. check api key')
        resultStr = "stt 오류입니다. 관리자에게 문의하세요 (DefaultCredentalsError)"
    else:
        resultStr = "undefined error. 관리자에게 문의하세요"
    finally:
        return HttpResponse(resultStr)
# client 접속 ip 확인하기
