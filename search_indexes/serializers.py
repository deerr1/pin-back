import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import PinDocument

class PinDocumentSerializer(DocumentSerializer):

    class Meta:
        document = PinDocument
        fields = (
            'id',
            'name',
            'description',
            'image',
            'upload_date',
            'board',
            'user'
        )