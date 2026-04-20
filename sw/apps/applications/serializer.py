from rest_framework import serializers
from .models import Application
"""DRF — Django Rest Framework — библиотека для Python, 
предназначенная для разработки RESTful API (интерфейсов прикладного программирования) на основе фреймворка Django. 
Простыми словами, DRF — это способ связать серверное приложение с другими сервисами, 
предоставляя доступ к данным через стандартизированные методы"""

class ApplicationSerializer(serializers.ModelSerializer):  #создает сериализатор модели
    class Meta:
        model = Application
        fields = "__all__"                                 #сериализуем все поля модели