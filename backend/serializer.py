from rest_framework import serializers
from backend.models import QAPairEntry
from backend.models import TranslatorEntry


class TranslatorEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslatorEntry
        fields = ('key', 'value')


class QAPairEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = QAPairEntry
        fields = ('question', 'answer')


class AITDataSerialier(serializers.Serializer):

    question = serializers.CharField(max_length=200)
    answer = serializers.CharField(max_length=200)


class AIRequestSerializer(serializers.Serializer):

    type = serializers.CharField(max_length=200)
    question = serializers.CharField(max_length=200)

