from .model_loader import ModelLoader


class SentimentService:

    @staticmethod
    def analyze(text):

        model = ModelLoader.get_model()

        prompt = f"""
You are a sentiment analysis AI.

Analyze the following text.

Return ONLY one word.

POSITIVE
NEGATIVE
NEUTRAL

Text:
{text}
"""

        response = model.generate_content(prompt)

        sentiment = response.text.strip().upper()

        return {
            "text": text,
            "sentiment": sentiment
        }