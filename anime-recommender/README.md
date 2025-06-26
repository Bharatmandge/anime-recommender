# 🎌 Anime Recommender System

An AI-powered content-based recommendation system that suggests similar anime based on **genre**, **type**, and **title** using **TF-IDF** and **cosine similarity**.

---
Link to the DataSets : https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

## 🛠️ Built with:
- 🐍 Python
- 🧠 Scikit-learn
- 🌐 Streamlit
- 📊 Pandas
- 💾 JSON
- 🧪 Jupyter (for EDA)

---

## 📁 Project Structure

anime-recommender/
├── app/
│ └── streamlit_app.py # Streamlit frontend
├── data/
│ ├── processed/
│ │ ├── cleaned_data.csv # ❗Removed due to GitHub's file size limit
│ │ └── anime_recommendations.json # Precomputed top-10 recommendations
│ └── raw/
│ ├── anime.csv # ✅ Kaggle dataset (Download required)
│ └── rating.csv # ❗Removed due to GitHub's file size limit
├── notebooks/
│ └── 01_eda.ipynb # Exploratory Data Analysis
├── src/
│ ├── data_cleaning.py # Raw to clean data
│ ├── model.py # Recommender system logic
│ └── precompute_similarity.py # Precomputes top-N similar anime
├── .gitignore
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🚀 Features

- 🔍 Recommends similar anime using text-based features  
- ⚡ Precomputes top-10 recommendations to avoid delay during runtime  
- 🎨 Streamlit UI for interactive use  
- 📉 Clean and EDA-ready structure  
- 📂 Modular code organization  

---

## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/Bharatmandge/anime-recommender.git
cd anime-recommender
Install dependencies
Make sure you're using Python 3.9+

bash
Copy
Edit
pip install -r requirements.txt
Download the Dataset

Due to GitHub's 100MB file limit, cleaned_data.csv and rating.csv were not uploaded.
➡️ Download the original dataset from Kaggle:
🎒 Kaggle Anime Dataset (by CooperUnion)

Precompute Similarities (Optional, but recommended)

bash
Copy
Edit
python src/precompute_similarity.py
Run the Streamlit App

bash
Copy
Edit
streamlit run app/streamlit_app.py
📦 Sample Usage
Search for an anime in the dropdown and hit "Get Recommendations".
You'll instantly see top 10 similar anime based on genre, type, and title!

📊 Algorithms Used
TF-IDF Vectorization

Cosine Similarity

Content-Based Filtering

📌 To-Do / Future Improvements
🎯 Add collaborative filtering

🧠 Use BERT or Sentence Transformers for semantic similarity

💾 Add user login for personalized history

📈 Deploy on Streamlit Cloud or Hugging Face Spaces

🙏 Credits
📊 Dataset: Kaggle - Anime Recommendations Database

Made with ❤️ by @Bharatmandge

