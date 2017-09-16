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

    # */backend/QA_API
    url(r'^QA_API', views.QA_Backend.as_view(), name='The Question/Answer API'),
    # url(r'^returnQA$', GetQAPair.as_view(), name='GetQAPair'),

    # /Chat/createQA
    # url(r'^createQA$', CreateQAPair.as_view(), name='CreateQAPair'),

    # /Chat/[Q Number_A Number]
    # url(r'^id=(?P<translateValue>[0-9]+)$', views.translate, name='get translate data'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
