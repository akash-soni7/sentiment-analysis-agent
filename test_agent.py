from sentiment_agent.sentiment_service import SentimentService


if __name__ == "__main__":
    text = input("Enter a sentence: ")

    result = SentimentService.analyze(text)

    print(result)