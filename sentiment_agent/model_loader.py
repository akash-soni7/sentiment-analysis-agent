# pyrefly: ignore [missing-import]
from transformers import pipeline


class ModelLoader:
    _classifier = None

    @classmethod
    def get_classifier(cls):
        if cls._classifier is None:
            print("Loading sentiment model...")

            cls._classifier = pipeline(
                task="sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )

            print("Model loaded successfully!")

        return cls._classifier