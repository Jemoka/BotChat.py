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