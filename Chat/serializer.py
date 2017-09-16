from rest_framework import serializers
from .models import TranslatorEntry
from .models import QAPairEntry


class TranslatorEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslatorEntry
        fields = ('key', 'value')


class QAPairEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = QAPairEntry
        fields = ('question', 'answer')