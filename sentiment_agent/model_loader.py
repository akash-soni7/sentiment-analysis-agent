import os
# pyrefly: ignore [missing-import]
import google.generativeai as genai
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv()


class ModelLoader:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

            cls._model = genai.GenerativeModel("gemini-2.5-flash")

        return cls._model