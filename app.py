import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Population Dashboard", layout="wide")

st.title("🌍 Global Population Dashboard")
st.markdown("Interactive visualization using public data")

# Dataset
url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"

df = pd.read_csv(url)

# Sidebar
countries = st.sidebar.multiselect(
    "Select Countries",
    df["Country Name"].unique(),
    default=["India", "China", "United States"]
)

filtered_df = df[df["Country Name"].isin(countries)]

# Line Chart
st.subheader("Population Growth")

line_chart = px.line(
    filtered_df,
    x="Year",
    y="Value",
    color="Country Name"
)

st.plotly_chart(line_chart, use_container_width=True)

# Latest Data
latest_year = filtered_df["Year"].max()

latest = filtered_df[filtered_df["Year"] == latest_year]

# Bar Chart
st.subheader("Latest Population Comparison")

bar_chart = px.bar(
    latest,
    x="Country Name",
    y="Value",
    color="Country Name"
)

st.plotly_chart(bar_chart, use_container_width=True)

# Pie Chart
st.subheader("Population Share")

pie_chart = px.pie(
    latest,
    names="Country Name",
    values="Value"
)

st.plotly_chart(pie_chart, use_container_width=True)
