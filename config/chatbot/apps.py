from django.apps import AppConfig
import pickle



class ChatbotConfig(AppConfig):
    name = 'chatbot'
    models = pickle.load(open("C:\\Users\\이주연\\iris_model.sav", "rb"))

