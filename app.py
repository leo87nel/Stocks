# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("fundamentals_with_metadata.csv")

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
