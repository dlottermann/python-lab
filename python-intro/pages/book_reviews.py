import streamlit as st
import pandas as pd

st.set_page_config(page_title='Book Reviews', page_icon='📚',
                   layout='wide')


df_review = pd.read_csv('data/reviews.csv')
df_trend = pd.read_csv('data/trending.csv')


books = df_trend['book title'].unique()
book = st.sidebar.selectbox('Books', books)

df_book = df_trend[df_trend['book title'] == book]
df_review = df_review[df_review['book name'] == book]

book_title = df_book['book title'].iloc[0]
book_author = df_book['author'].iloc[0]
book_price = df_book['book price'].iloc[0]
book_rating = df_book['rating'].iloc[0]
book_genre = df_book['genre'].iloc[0]
book_year = df_book['year of publication'].iloc[0]

st.title(book_title)
#st.header(f'Author: {book_author}')
st.subheader(f'{book_genre}')

column1, column2, column3 = st.columns(3)

column1.metric('Price', f'${book_price}')
column2.metric('Rating', f'{book_rating}')
column3.metric('Year', f'{book_year}')

st.divider()

df_review

for row in df_review.values:
    message = st.chat_message(f"{row[4]}")
    message.markdown(f"#### {row[2]}")
    message.write(row[5])
    message.write(f"reviewer: {row[3]}")