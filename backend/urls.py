"""
BotChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    # */backend/api/QA
    url(r'^api/QAPairs$', views.QA_Backend.as_view(), name='The Question/Answer API'),

    # */backend/api/TranslatePairs
    url(r'^api/TranslatorPairs', views.Translator_Backend.as_view(), name='The Translator API'),

    # */backend/Class_Backend
    url(r'^api/Class_Backend', views.Class_Backend.as_view(), name='The Class API'),

    # */backend/DB_Backend
    url(r'^api/DB_Backend', views.DB_Backend.as_view(), name='The Database API'),

    # */backend/AI_Backend
    url(r'^api/AI_Backend', views.AI_Backend.as_view(), name='The AI Engine'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
