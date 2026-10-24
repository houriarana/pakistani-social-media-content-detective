import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Graphs ban rahe hain...")

# Data load karein
df = pd.read_csv('processed_sentiment.csv')

# 1. Sentiment ka Pie Chart
plt.figure(figsize=(6,6))
df['sentiment'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#66b3ff','#99ff99','#ff9999'])
plt.title('Sentiment Distribution of Drama Comments')
plt.ylabel('') # Side ka label hatane ke liye
plt.savefig('sentiment_pie_chart.png')
plt.close()

# 2. Sentiment ka Bar Chart
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='sentiment', palette='viridis')
plt.title('Number of Comments by Sentiment')
plt.savefig('sentiment_bar_chart.png')
plt.close()

print("Mubarak ho! Graphs ki 2 pictures ban gayi hain.")