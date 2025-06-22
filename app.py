# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

#Create sample DataFrame manually
df = pd.DataFrame({
    "P/E Ratio": [10, 15, 20],
    "ROE": [0.1, 0.2, 0.15],
    "Sector": ["Tech", "Healthcare", "Finance"],
    "Country": ["USA", "USA", "Canada"],
    "Company Name": ["A Corp", "B Corp", "C Corp"],
    "Ticker": ["A", "B", "C"]
})

st.title("📊 Crossplot Dashboard")

x_axis = st.selectbox("Select X-axis", df.columns)
y_axis = st.selectbox("Select Y-axis", df.columns)
color_by = st.selectbox("Color by", ['Sector', 'Country', 'None'])

if x_axis and y_axis:
    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color=color_by if color_by != 'None' else None,
        hover_data=['Company Name', 'Ticker'],
        text='Ticker',
        title=f"{y_axis} vs {x_axis}"
    )
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)
