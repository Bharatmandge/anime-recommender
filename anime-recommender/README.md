# 🎌 Anime Recommender System

An AI-powered content-based recommendation system that suggests similar anime based on **genre**, **type**, and **title** using **TF-IDF** and **cosine similarity**.

Built with:
- 🐍 Python
- 🧠 Scikit-learn
- 🌐 Streamlit
- 📊 Pandas
- 💾 JSON
- 🧪 Jupyter (for EDA)

---

## 📁 Project Structure

```bash
anime-recommender/
├── app/
│   └── streamlit_app.py             # Streamlit frontend
├── data/
│   ├── processed/
│   │   ├── cleaned_data.csv         # Final cleaned dataset
│   │   └── anime_recommendations.json  # Precomputed top-10 recommendations
│   └── raw/
│       ├── anime.csv                # Raw anime data
│       └── rating.csv               # User ratings
├── notebooks/
│   └── 01_eda.ipynb                 # Exploratory Data Analysis
├── src/
│   ├── data_cleaning.py            # Raw to clean data
│   ├── model.py                    # Recommender system logic
│   └── precompute_similarity.py    # Precomputes top-N similar anime
├── .gitignore
├── requirements.txt
└── README.md
🚀 Features
🔍 Recommends similar anime using text-based features

⚡ Precomputes top-10 recommendations to avoid delay during runtime

🎨 Streamlit UI for interactive use

📉 Clean and EDA-ready data

📂 Modular code structure

🔧 Setup Instructions
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/Bharatmandge/anime-recommender.git
cd anime-recommender
2. Install dependencies
Make sure you’re using Python 3.9+
Then run:

bash
Copy
Edit
pip install -r requirements.txt
3. Precompute Similarities (optional but faster)
bash
Copy
Edit
python src/precompute_similarity.py
4. Run Streamlit App
bash
Copy
Edit
streamlit run app/streamlit_app.py
📦 Sample Usage
Search for an anime in the dropdown and hit "Get Recommendations".
You'll instantly see top 10 similar anime based on genre, type & title!

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
Dataset: Kaggle Anime Dataset
Made with ❤️ by @Bharatmandge

🧠 License
This project is open source and free to use under the MIT License.

yaml
Copy
Edit

---

### ✅ Bonus Tip:

Run this in your terminal to instantly create the file:
```bash
echo "" > README.md
notepad README.md
