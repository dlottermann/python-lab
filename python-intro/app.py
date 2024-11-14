import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Book Trending', page_icon='📚',
                   layout='wide')


df_review = pd.read_csv('data/reviews.csv')
df_trend = pd.read_csv('data/trending.csv')

df_books_max_price = df_trend['book price'].max()
df_books_min_price = df_trend['book price'].min()

max_price = st.sidebar.slider('Price Range', df_books_min_price,df_books_max_price, df_books_max_price)

df_books = df_trend[df_trend['book price'] <= max_price]

df_books

chart_bar = px.bar(df_books['year of publication'].value_counts())
chart_histogram = px.histogram(df_books, x='book price')


column1, column2 = st.columns(2)

column1.plotly_chart(chart_bar)
column2.plotly_chart(chart_histogram)