import pandas as pd
import streamlit as st
import altair as alt

# Load Excel
df = pd.read_excel("KDp.xlsx")

# Clean up currency symbols if needed
for col in ['Price', 'Invested', 'P/L']:
    df[col] = df[col].replace('[₹,]', '', regex=True).astype(float)

st.title("Stock Portfolio Dashboard")

# 1. P/L by Stock (bar chart)
pl_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Stock', sort='-y'),
    y='P/L',
    color=alt.condition(
        alt.datum['P/L'] > 0,
        alt.value('green'),
        alt.value('red')
    )
).properties(title="Profit / Loss by Stock")
st.altair_chart(pl_chart, use_container_width=True)

# 2. Portfolio allocation (pie chart)
alloc_chart = alt.Chart(df).mark_arc(innerRadius=60).encode(
    theta=alt.Theta(field="Invested", type="quantitative"),
    color=alt.Color(field="Stock", type="nominal"),
    tooltip=["Stock", "Invested"]
).properties(title="Portfolio Allocation by Investment")
st.altair_chart(alloc_chart, use_container_width=True)
