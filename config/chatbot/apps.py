from django.apps import AppConfig
import pickle
import os
from konlpy.tag import Komoran
from gensim.models import FastText
import requests
import urllib3
import json
from transformers import BertModel
from transformers import BertForQuestionAnswering
from tokenization_kobert import *
import torch


class ChatbotConfig(AppConfig):
    name = 'chatbot'
    komoran = Komoran()
    fmodel = FastText.load("400_5_4.model")
    bmodel = BertForQuestionAnswering.from_pretrained('models/checkpoint-24000/')
    btokenizer = KoBertTokenizer.from_pretrained('models/checkpoint-24000/')

    def answering(question,context,model,stoknizer):
        input_ids = stoknizer.encode(question,context)
        tokens = stoknizer.convert_ids_to_tokens(input_ids)
        if len(tokens)>512:
            return ""
        # 입력 임베딩 길이 초과

        tokens = stoknizer.convert_ids_to_tokens(input_ids)
        sep_index = input_ids.index(stoknizer.sep_token_id)

        # [SEP] 토큰 기준으로 질의, 문단 위치 파악
        num_seg_a = sep_index + 1
        num_seg_b = len(input_ids) - num_seg_a

        segment_ids = [0]*num_seg_a + [1]*num_seg_b

        # segment 토큰 반영
        assert len(segment_ids) == len(input_ids)
        start_scores, end_scores = model(torch.tensor([input_ids]),token_type_ids=torch.tensor([segment_ids]))
        # 시작 종료위치 계산
        answer_start = torch.argmax(start_scores)
        answer_end = torch.argmax(end_scores)

        # 가장 높은 확률의 토큰 위치 반환
        answer = ''.join(tokens[answer_start:answer_end+1])
        if len(answer) > 1:
            answer=answer[1:]
        # 시작 공백 문자 제거
        return answer.replace(" ","").replace("▁"," ")


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
