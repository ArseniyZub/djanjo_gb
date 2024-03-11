from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
 html = """
     <html>
     <head>
         <title>Добро пожаловать на мой первый сайт!</title>
     </head>
     <body>
         <h1>Добро пожаловать на главную страницу</h1>
         <p>Здесь вы найдете много интересного контента.</p>
     </body>
     </html>
     """
 log_data = "Посещена главная страница"
 logger.info(log_data)
 return HttpResponse(html)

def about(request):
 html = """
     <html>
     <head>
         <title>Информация обо мне</title>
     </head>
     <body>
         <h1>Обо мне</h1>
         <p>Привет, меня зовут Равиль и это мой первый Django-сайт.</p>
     </body>
     </html>
     """
 log_data = "Посещена страница 'о себе'"
 logging.info(log_data)
 return HttpResponse(html)