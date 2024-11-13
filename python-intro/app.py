import streamlit as st
import pandas as pd


st.set_page_config(page_title='Book Trending', page_icon='📚',
                   layout='wide')


df_review = pd.read_csv('data/reviews.csv')
df_trend = pd.read_csv('data/trending.csv')


df_review
