import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# 💡 Dynamically get the absolute path of the CSV file
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "processed", "cleaned_data.csv")

# ✅ Debugging help: print path being used
print("📂 Loading file from:", file_path)

# 🔁 Load the data
try:
    df = pd.read_csv(file_path)
    print("✅ File loaded successfully!")
except FileNotFoundError:
    print("❌ File not found! Check the path.")
    exit()

# ✅ Fill missing values (important for text vectorizer)
df['genre'] = df['genre'].fillna('')
df['type'] = df['type'].fillna('')
df['name'] = df['name'].fillna('')

# 🔗 Combine features for vectorization
df['combined_features'] = df['genre'] + " " + df['type'] + " " + df['name']

# ✨ TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

# 📊 Calculate cosine similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# 🎯 Recommendation Function
def recommend_anime(title, top_n=5):
    if title not in df['name'].values:
        return f"'{title}' not found in dataset."

    idx = df[df['name'] == title].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    anime_indices = [i[0] for i in sim_scores]
    return df['name'].iloc[anime_indices].tolist()

# 🔎 Example usage (Test it out!)
if __name__ == "__main__":
    anime_to_search = "Naruto"  # 👈 Change this to test others
    print(f"\n🎬 Recommendations for '{anime_to_search}':")
    recommendations = recommend_anime(anime_to_search)
    for i, rec in enumerate(recommendations, start=1):
        print(f"{i}. {rec}")
