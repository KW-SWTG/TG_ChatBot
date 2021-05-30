# 1. Introduction 
## AI 알고리즘을 활용한 챗봇 기반의 음성인식 서비스 개발
* 개발기간 : 2020.7.1 ~ 2021.5.31
* 팀명 : Team TG
* 팀원 : 신승수, 설지우, 이주연, 김현성
<br>

## [ 프로그램 소개 ]
프로젝트의 목표는 법률에 대한 사용자의 높은 접근성을 유지하면서 즉각적인 대응을 제공하는 챗봇을 개발하려 한다. 법무부에서 제공하는 약 4200여개의 법령과 9300여개의 정부 각 기관 행정규칙을 정제한 생활법령 데이터를 사용하고, 카카오 i builder나 구글의 dialogflow와 같은 기존 챗봇 프레임워크를 사용하는 것이 아닌 문서 검색과 딥러닝 기반의 기계독해 모델이 결합한 cdQA구조를 채택하여 좁은 도메인에 대해서만 응답이 가능하던 한계를 극복한다. 마지막으로 STT/TTS를 이용한 입출력을 통해, 텍스트뿐만 아니라 음성으로도 질의응답이 가능하게 하여 사용자 친화 인터페이스를 제공한다. 결과적으로 시간과 장소에 구애받지 않고, 사용자의 생활법률에 대한 궁금증을 해소하며 인공지능 언어모델을 사용한 웹 어플리케이션 형태의 챗봇 서비스를 구축하는 것이 최종목표이다.
<br><br>


# 2. 설계
<p align="center"><img src="https://user-images.githubusercontent.com/39071676/120092428-acc27600-c14d-11eb-8fa1-db3d952c9758.png"></p>
<br>
 Closed-domain Question&Answering 구조의 챗봇 구조를 채택하여 사용자의 질의를 음성 혹은 텍스트로 입력받는다. 해당 질의와 데이터 셋에서 질의에 답변이 포함 될 문단을 탐색한다. 이를 Document Retrival라고 지칭한다. 매칭 이후 해당 질의와 문단을 딥러닝 기반의 기계독해(MRC) 모델에 전달하여 답변을 획득하고, 이를 사용자에게 텍스트와 음성으로 제공한다. 
 <br><br>
 
# 3. 최종 결과물
시연영상 : https://www.youtube.com/watch?v=1S-ZDPKT9kE&t=2s
<p align="center">
<img src="https://user-images.githubusercontent.com/39071676/120092537-a7196000-c14e-11eb-972c-789bb435e471.png">
<img src="https://user-images.githubusercontent.com/39071676/120092545-b698a900-c14e-11eb-92de-a81069f9b60d.png">
</p>
<br><br> 

# 4. 예시 질문
총 204개 분야의 생활법령에 대한 질의응답이 가능합니다. 분야는 가족관계 등록, 상속, 자동차, 노인복지, 과태료 납부자 등이 있습니다. <br>
※ [찾기쉬운 생활법령정보 사이트 > 주제별 생활법령](https://www.easylaw.go.kr/CSP/CsmSortRetrieveLst.laf?sortType=cate&search_put=)를 참고하세요. 
  
**◎ “주택임대차”에 대한 질의** <br>
Q. 중개업소를 통해 주택임대차계약을 한 경우에는 어떤 서류를 받아야 하나요? <br>
A. 주택임대차계약서, 중개대상물 확인설명서, 공제증서 <br>
<br>

**◎ “소음ㆍ진동”에 대한 질의** <br>
Q. 도로 및 철도소음·진동 대상지역의 구분은 어떤 법률에서 확인할 수 있나요? <br> 
A. 국토의 계획 및 이용에 관한 법률 제36조 및 국토의 계획 및 이용에 관한 법률 시행령 제30조 <br>
<br>

**◎ “음식점 운영”에 대한 질의** <br>
Q. 광운대 앞에서 닭볶음탕 음식점을 운영하고 있는데 한달 전에 음식점위생등급 지정을 받았었습니다. 그러면 만약 제가 영업장 소재지를 변경한 경우에는 다른 절차가 필요하나요? <br>
A. 이전 한 날로부터 30일 이내에 품접객업소 위생등급 지정사항 변경신청서에 영업신고증, 위생등급지정서 및 위생등급표지판을 첨부하여 지정기관에 제출 <br>
<br>

**◎ “부동산”에 대한 질의** <br>
Q. 부동산에 관한 물권을 명의수탁자의 명의로 등기하면 어떻게 되나요? <br>
A. 5년 이하의 징역 또는 2억원 이하의 벌금 <br>
<br>

**◎ “고객응대 근로자”에 대한 질의** <br>
Q. 고객응대 근로자가 산업재해로 인정받을 수 있는 질병은 어떤 것들이 있나요? <br>
A. 적응장애, 우울병 에피소드, 외상 후 스트레스 장애 <br>
<br>

**◎ “반려동물과 생활하기”에 대한 질의** <br>
Q. 반려동물이 죽으면 사체처리는 어떻게 하나요?  <br>
A. 동물병원에서 자체적으로 처리되거나 폐기물처리업자 또는 폐기물처리시설 설치·운영자 등에게 위탁해서 처리 <br>
<br>

**◎ “특허권”에 대한 질의** <br>
Q. 국제특허를 받고자 하는 경우 PCT 출원절차는 어떤 순으로 진행되나요? <br>
A. 1. 국제출원, 2. 국제조사, 3. 국제공개, 4. 국제예비심사 <br>
<br>

**◎ “학교폭력”에 대한 질의** <br>
Q. 학교폭력 신고내용 누설 시 어떤 처벌을 받나요? <br>
A. 1년 이하의 징역 또는 1천만원 이하의 벌금  <br>
<br>

**◎ “해외유학자”에 대한 질의** <br>
Q. 해외유학자가 외국에서 국회의원선거에 대한 국외부재자 투표를 하기 위해서는 어떤 조건이 있어야 하나요? <br>
A. 국내에 주민등록이 되어 있어야 하고, 국외부재자로 신고 <br>
<br>

**◎ “시간선택제 근로자”에 대한 질의** <br>
Q. 채용형 시간선택제가 시간선택제 근로자를 신규로 채용하는 건 알겠는데 무슨 목적으로 운영되는 거야? <br>
A.. 피크타임 해소, 장시간 직무 분할, 우수 인력 확보, 근로자의 일·가정 양립 지원 등을 위해 <br>
<br><br> 

# 5. 활용한 오픈소스SW
 **Web Speech Synthesis**
- License : CC0-1.0 license
- URL : https://github.com/mdn/web-speech-api
- Chrome과 Firefox 웹 브라우저 상에서 텍스트를 음성으로 변환하여 출력
<br>

**Opus-media-recoder**
- License : MIT license
- URL : https://github.com/kbumsik/opus-media-recorder
- ES6와 WebAssembly에서 작성된 MediaRecorder API. Ogg, WebM 등 다양한 오디오 포맷을 가진 크로스 브라우저 Opus 코덱을 지원
<br>

**SKTBrain/KoBERT**
- License : Apache License 2.0
- URL : https://github.com/SKTBrain/KoBERT
- 한국어 위키에서 문장 5M, 단어 54M로 사전학습한 한국어형 Bert 모델
<br>

**FastText**
- License : MIT License
- URL : https://github.com/facebookresearch/fastText
- n-gram 방식을 차용한 분산표현 기반의 워드 임베딩 모델
<br>

**KorQuad 1.0**
- License : CC BY-ND 2.0KR
- URL : https://korquad.github.io/KorQuad%201.0/
- 기계독해를 위한 한국형 SQuaD Set
<br>

**skicit-learn**
-  License : 3-Clause BSD license
-  URL : https://github.com/scikit-learn/scikit-learn
-  python 기반의 오픈소스 기계학습 라이브러리. 지원 벡터 머신, 랜덤 포레스트, 그레디언트 부스팅, K-means 및 DBSCAN을 포함한 다양한 분류, 회귀, 클러스터링 알고리즘을 제공. 
<br>

**KoNLPy**
-  License : GNU General Public license
-  URL : https://github.com/konlpy/konlpy
-  한국어 자연어처리를 할 수 있는 파이썬 패키지. Hannanum, Kkma, Komoran, Mecab, Okt(구 Twitter) 5가지 형태소 분석 방법을 제공. 
<br>

**Django** 
-  License : BSD license
-  URL : https://github.com/django/django
-  python 기반의 오픈소스 웹 프레임워크. 풀스택 프레임워크로 프론트엔드, 백엔드의 개발을 모두 지원하기 때문에 웹 개발에서 내장된 기능만을 이용해 빠른 개발 가능. 
