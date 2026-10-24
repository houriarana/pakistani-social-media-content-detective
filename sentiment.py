import pandas as pd
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

print("Data load ho raha hai...")
# 1. Raw comments load karein
df = pd.read_csv('raw_comments.csv')

# 2. Data Cleaning (Saaf karna)
# Khali comments hata dein
df = df.dropna(subset=['comment'])
# Duplicate (repeat) comments hata dein
df = df.drop_duplicates(subset=['comment'])

def clean_text(text):
    text = re.sub(r'http\S+', '', str(text)) # Links hatao
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Sirf english letters rakho
    return text.strip().lower()

df['cleaned_comment'] = df['comment'].apply(clean_text)

print("Sentiment Analysis chal rahi hai... (Thora waqt lagega)")
# 3. Sentiment Analysis (Positive, Negative, Neutral)
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['cleaned_comment'].apply(get_sentiment)

# 4. Processed file save karein
df.to_csv('processed_sentiment.csv', index=False)

print("Kaam mukammal! 'processed_sentiment.csv' file ban gayi hai.")
print("Sentiment Count:")
print(df['sentiment'].value_counts())