from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

text = "The new AI-powered chatbot is absolutely best and very helpful!"
sentiment = sentiment_analyzer(text)

print("Sentiment:", sentiment[0]['label'], "with confidence:", sentiment[0]['score'])
