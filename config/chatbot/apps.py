from django.apps import AppConfig
import pickle
import os
from konlpy.tag import Komoran
from gensim.models import FastText
import requests
import urllib3
import json


class ChatbotConfig(AppConfig):
    name = 'chatbot'
    komoran = Komoran()
    fmodel = FastText.load("VV_sg_100_3_5.model")

    def hyapi(Q):
        key = '5d8c5655-dfcc-4eff-9eda-9c4b959603af'
        url = "http://aiopen.etri.re.kr:8000/WikiQA"
        question = Q
        qtype = "hybridqa"

        requestJson = {
            "access_key": key,
            "argument": {
                "question": question,
                "type": qtype
            }
        }
        http = urllib3.PoolManager()

        response = http.request(
            "POST",
            url,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson)
        )

        print("[responseCode] " + str(response.status))
        print("[responBody]")
        print(str(response.data, "utf-8"))
        print(response.data, "utf-8")
        data = json.loads(response.data)
        answer = data['return_object']['WiKiInfo']['AnswerInfo']
        # confidence = data['return_object']['WiKiInfo']['Confidence']
        print(answer)
        if answer == []:
            return "답변을 출력할 수 없습니다."
        else:
            print()
            print(answer[0]['answer'], answer[0]['confidence'])
            return str(answer[0]['answer'])

    def mrc2api(Q, paragraph):
        key = '5d8c5655-dfcc-4eff-9eda-9c4b959603af'
        url = "http://aiopen.etri.re.kr:8000/MRCServlet"
        question = Q
        para = paragraph

        requestJson = {
            "access_key": key,
            "argument": {
                "question": question,
                "passage": para
            }
        }
        http = urllib3.PoolManager()

        response = http.request(
            "POST",
            url,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson)
        )

        print("[responseCode] " + str(response.status))
        print("[responBody]")
        print(str(response.data, "utf-8"))
        data = json.loads(response.data)
        answer = data['return_object']['MRCInfo']['answer']
        if answer == []:
            return "답변을 출력할 수 없습니다."
        else:
            return answer

    def load_cate():
        flst = os.listdir("filter1_ver4")
        category = []
        for i in flst:
            category.append(i.replace(".csv", ""))
        return category
