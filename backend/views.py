from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from .models import TranslatorEntry
from .models import QAPairEntry
from .AIEngine import AIEngine, DatabaseModule
from django.db.models import Max

# The database backend
class QA_Backend(APIView):
    def get(self, request):
        queryset = QAPairEntry.objects.all()
        serializer = QAPairEntrySerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = QAPairEntrySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Translator_Backend(APIView):
    def get(self, request):
        queryset = TranslatorEntry.objects.all()
        serializer = TranslatorEntrySerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = TranslatorEntrySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DB_Backend(APIView):
    def put(self, request):
        serializer = AITDataSerialier(data=request.data, many=False)
        if serializer.is_valid():
            data = serializer.data
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        dbmodule = DatabaseModule()
        print("ran! q:"+list(data.values())[0]+"a"+list(data.values())[1])
        dbmodule.storeQAPair(question_entry=list(data.values())[0], answer_entry=list(data.values())[1])
        return Response(status.HTTP_200_OK)


class AI_Backend(APIView):
    def put(self, request):
        serializer = AIRequestSerializer(data=request.data, many=False)
        if serializer.is_valid():
            data = serializer.data
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        engine = AIEngine(type=list(data.values())[0])
        print("RESPONSE:"+engine.predictAnswer(list(data.values())[1]))
        return Response(engine.predictAnswer(list(data.values())[1]))

