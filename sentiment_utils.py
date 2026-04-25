import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


def fetch_news(company_name, api_key):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": company_name,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 20,
        "apiKey": api_key,
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        return data.get("articles", [])
    except Exception:
        return []


def classify_sentiment(score):
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    return "Neutral"


def analyze_articles(articles):
    rows = []

    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        content = f"{title}. {description}"

        if not content.strip():
            continue

        score = analyzer.polarity_scores(content)["compound"]
        sentiment = classify_sentiment(score)

        rows.append({
            "title": title,
            "description": description,
            "source": article.get("source", {}).get("name", "Unknown"),
            "publishedAt": article.get("publishedAt", ""),
            "url": article.get("url", ""),
            "score": score,
            "sentiment": sentiment,
        })

    return pd.DataFrame(rows)