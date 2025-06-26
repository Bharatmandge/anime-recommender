import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from tqdm import tqdm

print("🔥 Starting Smart Precompute...")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "processed", "cleaned_data.csv")

df = pd.read_csv(file_path, low_memory=False)

# ✅ Cut it down to 2000 for survival
df = df.head(2000)

df['genre'] = df['genre'].fillna('')
df['type'] = df['type'].fillna('')
df['name'] = df['name'].fillna('')
df['combined'] = df['genre'] + " " + df['type'] + " " + df['name']

print("✍️ Vectorizing... (2000 rows only)")
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

print("⚡ Calculating top-10 similarities...")
recommendations = {}
for i in tqdm(range(len(df))):
    sim_scores = cosine_similarity(tfidf_matrix[i], tfidf_matrix).flatten()
    sim_scores[i] = -1
    top_indices = sim_scores.argsort()[-10:][::-1]
    recs = df['name'].iloc[top_indices].tolist()
    recommendations[df['name'].iloc[i]] = recs

output_path = os.path.join(base_dir, "data", "processed", "anime_recommendations.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(recommendations, f, indent=4, ensure_ascii=False)

print("✅ DONE! Recommendations saved.")
