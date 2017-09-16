from django.shortcuts import get_object_or_404
from rest_framework.generics import (CreateAPIView,DestroyAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import TranslatorEntrySerializer
from .serializer import QAPairEntrySerializer
from  .models import TranslatorEntry
from .models import QAPairEntry

# The chatting backend
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
