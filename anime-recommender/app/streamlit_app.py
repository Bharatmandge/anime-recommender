import streamlit as st
import pandas as pd
import os 
import json 

@st.cache_data 
def load_data():
     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     data_path = os.path.join(base_dir, "data", "processed", "cleaned_data.csv")
     json_path = os.path.join(base_dir, "data", "processed", "anime_recommendations.json")
        
     df = pd.read_csv(data_path)
     with open(json_path, "r", encoding="utf-8") as f:
            recommendations = json.load(f)
     return df, recommendations
    
# Recommendation Function 
def get_recommendations(title,reco_dict):
    return reco_dict.get(title,[])

#UI 
st.set_page_config(page_title="Anime Recommender",page_icon="🍥")
st.title("🎌 Anime Recommender System")
st.markdown("Enter your favorite anime  and get recommendation based on genre,type and title.")

#load 
df, reco_dict = load_data()

anime_list = sorted(df['name'].dropna().unique())
selected_anime = st.selectbox("🔎 Choose an anime you love:", anime_list)

if st.button("💡 Recommend Similar Anime"):
    recos = get_recommendations(selected_anime,reco_dict)
    if recos:
        st.success("✨ You might also enjoy:")
        for i, anime in enumerate(recos,1):
            st.write(f"{i}. {anime}")
    else:
        st.warning("No recommendation bro watch better anime ")