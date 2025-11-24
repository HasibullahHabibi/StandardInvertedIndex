import re

STOPWORDS = {"the", "is", "are", "was", "were", "in", "on", "with", "and", "a", "an"}

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize(text):
    tokens = [word for word in text.split() if word not in STOPWORDS]
    return tokens
