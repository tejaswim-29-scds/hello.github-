
# Step 1: Import the required libraries

import streamlit as st
import pandas as pd


# Step 2: Display the dashboard title

st.title("IMDb Top 250 Movies Dashboard")


# Step 3: Load the CSV dataset

movies = pd.read_csv("C:\Users\yaswa\Streamlit.lab\ToP 250 movies on imdb in 2026-selected-columns.csv")


# Step 4: Display a success message

st.success("Dataset loaded successfully!")


# Step 5: Display the first 10 rows

st.subheader("First 10 Movies")

st.dataframe(movies.head(10))


# Step 6: Display the number of rows and columns

st.subheader("Dataset Shape")

st.write("Number of Rows:", movies.shape[0])

st.write("Number of Columns:", movies.shape[1])


# Step 7: Display all column names

st.subheader("Column Names")

st.write(movies.columns.tolist())


# Step 8: Display column data types

st.subheader("Column Data Types")

st.write(movies.dtypes)


# Step 9: Display missing values

st.subheader("Missing Values")

st.write(movies.isnull().sum())
