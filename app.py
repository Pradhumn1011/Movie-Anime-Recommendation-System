import streamlit as st
import pickle
import pandas as pd


def recommend(option):
    if option_1=="Movies":
        movie_index = movies[movies['title'] == option].index[0]
        distances = s_score[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended=[]
        for i in movies_list:
            movie_id=movies.iloc[i[0]]['movie_id']
            recommended.append(movies.iloc[i[0]]['title'])

    else:
        anime_index = animes[animes['Name'] == option].index[0]
        distances = similarity[anime_index]
        anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended=[]
        for i in anime_list:
            recommended.append(animes.iloc[i[0]]['Name'])
    return recommended


movies_list=pickle.load(open('../pythonProject/movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
animes_list=pickle.load(open('../pythonProject/animes.pkl','rb'))
animes=pd.DataFrame(animes_list)
similarity=pickle.load(open('../pythonProject/similarity.pkl','rb'))
s_score=pickle.load(open('../pythonProject/s_score.pkl','rb'))

st.title("Recommendation System")
option_1=st.selectbox('What would you like to watch today?',["Movies","Anime"])
if option_1=='Movies':
    option_2 = st.selectbox('Please Select your latest watch: ', movies['title'].values)
else:
    option_2 = st.selectbox('Please Select your latest watch:- ', animes['Name'].values)

if st.button('Recommend'):
    recommendations=recommend(option_2)
    for i in recommendations:
        st.write(i)
