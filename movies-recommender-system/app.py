import streamlit as st
import pickle
import pandas as pd
import zipfile
import os

st.write("Files in current directory:", os.listdir("."))
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
with zipfile.ZipFile("similarity.zip", "r") as zip_ref:
    with zip_ref.open("similarity.pkl") as f:
        similarity = pickle.load(f)
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
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
