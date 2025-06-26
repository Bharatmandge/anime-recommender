import pandas as pd
import os

def load_data(anime_path: str,rating_path: str):
    anime = pd.read_csv(anime_path)
    ratings = pd.read_csv(rating_path)
    return anime, ratings

def clean_anime_data(anime_df: pd.DataFrame) -> pd.DataFrame:
    anime_df.dropna(inplace=True)
    anime_df = anime_df[anime_df['rating'] > 0]
    return anime_df

def clean_rating_data(rating_df: pd.DataFrame) -> pd.DataFrame:
    return rating_df[rating_df['rating'] != -1]

def merge_datasets(anime_df, rating_df):
    merged = pd.merge(rating_df, anime_df, on='anime_id')
    return merged
def save_cleaned_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    
    
if __name__ == "__main__":
    anime_path = "data/raw/anime.csv"
    rating_path = "data/raw/rating.csv"
    output_path = "data/processed/cleaned_data.csv"
    
    anime_df, rating_df = load_data(anime_path, rating_path)
    anime_df = clean_anime_data(anime_df)
    rating_df = clean_rating_data(rating_df)
    final_df = merge_datasets(anime_df, rating_df)
    save_cleaned_data(final_df, output_path)