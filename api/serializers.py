# pyrefly: ignore [missing-import]
from rest_framework import serializers


class SentimentSerializer(serializers.Serializer):
    text = serializers.CharField(
        max_length=1000,
        required=True
    )


class BatchSentimentSerializer(serializers.Serializer):
    texts = serializers.ListField(
        child=serializers.CharField(max_length=1000),
        allow_empty=False
    )