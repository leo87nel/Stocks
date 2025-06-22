{
 "cells": [
  {
   "cell_type": "code",
   "id": "6bd5bca0-1323-421c-9f9e-48aa1382d21b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app.py\n",
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "# Load a sample DataFrame (replace this with your real data)\n",
    "df = pd.read_csv(\"fundamentals_with_metadata.csv\")\n",
    "\n",
    "st.title(\"📊 Crossplot Dashboard\")\n",
    "\n",
    "x_axis = st.selectbox(\"Select X-axis\", df.columns)\n",
    "y_axis = st.selectbox(\"Select Y-axis\", df.columns)\n",
    "color_by = st.selectbox(\"Color by\", ['Sector', 'Country', 'None'])\n",
    "\n",
    "if x_axis and y_axis:\n",
    "    fig = px.scatter(\n",
    "        df,\n",
    "        x=x_axis,\n",
    "        y=y_axis,\n",
    "        color=color_by if color_by != 'None' else None,\n",
    "        hover_data=['Company Name', 'Ticker'],\n",
    "        text='Ticker',\n",
    "        title=f\"{y_axis} vs {x_axis}\"\n",
    "    )\n",
    "    fig.update_traces(textposition='top center')\n",
    "    st.plotly_chart(fig, use_container_width=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
