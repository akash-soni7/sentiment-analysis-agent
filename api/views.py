# pyrefly: ignore [missing-import]
from rest_framework.views import APIView
# pyrefly: ignore [missing-import]
from rest_framework.response import Response
# pyrefly: ignore [missing-import]
from rest_framework import status

from .serializers import (
    SentimentSerializer,
    BatchSentimentSerializer
)

from sentiment_agent.sentiment_service import SentimentService


class HealthCheckView(APIView):

    def get(self, request):

        return Response(
            {
                "success": True,
                "message": "API is running",
                "model_loaded": True
            }
        )


class AnalyzeSentimentView(APIView):

    def post(self, request):

        serializer = SentimentSerializer(data=request.data)

        if serializer.is_valid():

            text = serializer.validated_data["text"]

            result = SentimentService.analyze(text)

            return Response(
                {
                    "success": True,
                    "data": result
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BatchAnalyzeView(APIView):

    def post(self, request):

        serializer = BatchSentimentSerializer(data=request.data)

        if serializer.is_valid():

            texts = serializer.validated_data["texts"]

            results = []

            for text in texts:
                results.append(
                    SentimentService.analyze(text)
                )

            return Response(
                {
                    "success": True,
                    "count": len(results),
                    "results": results
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ModelInfoView(APIView):

    def get(self, request):

        return Response(
            {
                "model":
                "distilbert-base-uncased-finetuned-sst-2-english",

                "framework":
                "HuggingFace Transformers",

                "labels":
                [
                    "POSITIVE",
                    "NEGATIVE"
                ]
            }
        )