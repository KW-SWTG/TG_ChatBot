from django.apps import AppConfig
import pickle
import os


class ChatbotConfig(AppConfig):
    name = 'chatbot'
    # credential_path = "C:\\Users\\이주연\\Desktop\\깃허브\\config\\chatbot\\chatbot-stt-b7d997126b9b.json"
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    models = pickle.load(open("C:\\Users\\이주연\\iris_model.sav", "rb"))

