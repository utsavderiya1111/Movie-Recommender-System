import streamlit as st
import pickle
import pandas as pd
import zipfile
import os

BASE_DIR = "movies-recommender-system"
zip_path = os.path.join(BASE_DIR, "similarity.zip")
movie_dict_path = os.path.join(BASE_DIR, "movie_dict.pkl")
st.write("Files in movies-recommender-system folder:", os.listdir(BASE_DIR))
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
# ✅ Check if file exists
# Paths for files inside folder

# ✅ Check similarity.zip
if os.path.exists(movie_dict_path):
    st.write("movie_dict.pkl size:", os.path.getsize(movie_dict_path))

    with open(movie_dict_path, "rb") as f:
        header = f.read(20)  # read first 20 bytes
        st.write("First 20 bytes of movie_dict.pkl:", header)
        f.seek(0)  # reset file pointer
        try:
            movies_dict = pickle.load(f)
        except Exception as e:
            st.error(f"Unpickling failed: {e}")
            st.stop()

else:
    st.error(f"File not found: {zip_path}")
    st.stop()

# ✅ Check movie_dict.pkl
if os.path.exists(movie_dict_path):
    with open(movie_dict_path, "rb") as f:
        movies_dict = pickle.load(f)
else:
    st.error(f"File not found: {movie_dict_path}")
    st.stop()

movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select Movie',
    movies['title'].values
)

if st.button('Recommend Movie'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
