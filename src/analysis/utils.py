from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😀"
    elif polarity < 0:
        return "Negative 🙁"
    else:
        return "Neutral 😐"

from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    if len(text.split()) < 30:  # Ensure text has enough words to summarize
        return "Text is too short to summarize."
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']