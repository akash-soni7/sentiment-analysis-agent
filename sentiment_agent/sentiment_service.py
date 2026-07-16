from .model_loader import ModelLoader


class SentimentService:

    @staticmethod
    def analyze(text: str):
        classifier = ModelLoader.get_classifier()

        result = classifier(text)[0]

        return {
            "text": text,
            "sentiment": result["label"],
            "confidence": round(result["score"], 4)
        }