import pandas as pd
import streamlit as st
import altair as alt

# Load Excel file from root directory
df = pd.read_excel("KDp.xlsx")  # replace with your filename

# Streamlit app
st.title("Excel Data Visualization")
st.write(df.head())

# Example Altair chart
chart = alt.Chart(df).mark_bar().encode(
    x='Price',  # replace with your column name
    y='Invested'
)
st.altair_chart(chart, use_container_width=True)
