import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Year selector
min_year = int(df['year'].min())
max_year = int(df['year'].max())

year_range = st.slider(
    "Select publication year range:",
    min_year,
    max_year,
    (min_year, max_year)
)

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write("### Sample of filtered data")
st.write(filtered.head())

# Visualization: Publications by Year
st.write("## Publications by Year")

year_counts = filtered['year'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Publication Count")
st.pyplot(fig)
