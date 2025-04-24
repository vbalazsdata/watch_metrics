import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from utils import get_data




# Adatok betöltése
df = get_data()

st.markdown("## Visualize your data insights through interactive charts")
st.markdown("Explore trends, correlations, and patterns with dynamic graphs to make data analysis easier and more intuitive.")

st.markdown("---")  # Optional: visual separator
# Oldalcím
st.title("Metrics Overview")

# Másolat a DataFrame-ből, amit szűrni fogunk
filtered_df = df.copy()

st.sidebar.header("🔍 Filters")

def sort_values_with_nan(values):
    """Segédfüggvény a NaN értékek kezelésére és a rendezésre"""
    sorted_values = sorted([v for v in values if pd.notna(v)]) + [v for v in values if pd.isna(v)]
    return sorted_values

# Márka szűrő (dropdown)
brands = df["Brand"].unique().tolist()
brands = sort_values_with_nan(brands)
brands.insert(0, "All values")
st.sidebar.markdown("**Brand**")
selected_brand = st.sidebar.selectbox("", options=brands)
if selected_brand != "All values":
    filtered_df = filtered_df[filtered_df["Brand"] == selected_brand]

# Modell szűrő (dropdown)
models = filtered_df["Model"].unique().tolist()
models = sort_values_with_nan(models)
models.insert(0, "All values")
st.sidebar.markdown("**Model**")
selected_model = st.sidebar.selectbox("", options=models)
if selected_model != "All values":
    filtered_df = filtered_df[filtered_df["Model"] == selected_model]

# Működés szűrő (dropdown)
movements = filtered_df["Movement"].unique().tolist()
movements = sort_values_with_nan(movements)
movements.insert(0, "All values")
st.sidebar.markdown("**Movement**")
selected_movement = st.sidebar.selectbox("", options=movements)
if selected_movement != "All values":
    filtered_df = filtered_df[filtered_df["Movement"] == selected_movement]

# Gyártási év szűrő (dropdown)
if "Year of production" in filtered_df.columns and not filtered_df["Year of production"].isna().all():
    years = sort_values_with_nan(sorted(filtered_df["Year of production"].dropna().unique().tolist()))
    years.insert(0, "All values")
    st.sidebar.markdown("**Year of production**")
    selected_year = st.sidebar.selectbox("", options=years)
    if selected_year != "All values":
        filtered_df = filtered_df[filtered_df["Year of production"] == selected_year]

# Fellelhetőség szűrő (dropdown)
locations = filtered_df["Location"].unique().tolist()
locations = sort_values_with_nan(locations)
locations.insert(0, "All values")
st.sidebar.markdown("**Location**")
selected_location = st.sidebar.selectbox("", options=locations)
if selected_location != "All values":
    filtered_df = filtered_df[filtered_df["Location"] == selected_location]

# Ellenőrizzük, hogy van-e adat a szűrés után
if filtered_df.empty:
    st.write("No results found.")
else:
    # Márka bar chart with Plotly
    st.write("### 📊 Distribution of Brands")
    marca_counts = filtered_df['Brand'].value_counts()
    
    marca_fig = go.Figure([go.Bar(
        x=marca_counts.index,
        y=marca_counts.values,
        marker_color='#262626'  # Dark gray color
    )])
    marca_fig.update_layout(
        #title="Number of advertisements by Brand",
        xaxis_title="Brand",
        yaxis_title="Number of Advertisements",
        height=300,  # Smaller height for a more compact plot
        margin=dict(l=20, r=20, t=40, b=60),  # Adjust margins
        xaxis_tickangle=-45,  # Rotate x-axis labels for readability
        plot_bgcolor="#ffffff",  # Light background
        paper_bgcolor="#ffffff",  # White paper background
        font=dict(color="#262626")  # Dark font color
    )
    st.plotly_chart(marca_fig, use_container_width=True)

    # Működése bar chart with Plotly
    st.write("### 📊 Distribution by Movement")
    movement_counts = filtered_df['Movement'].value_counts()
    
    movement_fig = go.Figure([go.Bar(
        x=movement_counts.index,
        y=movement_counts.values,
        marker_color='#262626'  # Dark gray color
    )])
    movement_fig.update_layout(
        #title="Number of advertisements by Movement",
        xaxis_title="Movement",
        yaxis_title="Number of Advertisements",
        height=300,  # Smaller height for a more compact plot
        margin=dict(l=20, r=20, t=40, b=60),  # Adjust margins
        xaxis_tickangle=-45,  # Rotate x-axis labels for readability
        plot_bgcolor="#ffffff",  # Light background
        paper_bgcolor="#ffffff",  # White paper background
        font=dict(color="#262626")  # Dark font color
    )
    st.plotly_chart(movement_fig, use_container_width=True) 




