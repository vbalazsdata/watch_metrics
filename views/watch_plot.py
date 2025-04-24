import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from utils import get_data

# Loading data
df = get_data()

# Page title
st.title("Metrics Overview")

st.markdown("## Visualize your data insights through interactive charts")
st.markdown("Explore trends, correlations, and patterns with dynamic graphs to make data analysis easier and more intuitive.")

# Creating a copy of the DataFrame for filtering
filtered_df = df.copy()

st.sidebar.header("🔍 Filters")

def sort_values_with_nan(values):
    sorted_values = sorted([v for v in values if pd.notna(v)]) + [v for v in values if pd.isna(v)]
    return sorted_values

# Brnand filter (dropdown)
brands = df["Brand"].unique().tolist()
brands = sort_values_with_nan(brands)
brands.insert(0, "All values")
st.sidebar.markdown("**Brand**")
selected_brand = st.sidebar.selectbox("", options=brands)
if selected_brand != "All values":
    filtered_df = filtered_df[filtered_df["Brand"] == selected_brand]

# Model filter (dropdown)
models = filtered_df["Model"].unique().tolist()
models = sort_values_with_nan(models)
models.insert(0, "All values")
st.sidebar.markdown("**Model**")
selected_model = st.sidebar.selectbox("", options=models)
if selected_model != "All values":
    filtered_df = filtered_df[filtered_df["Model"] == selected_model]

# Movement filter (dropdown)
movements = filtered_df["Movement"].unique().tolist()
movements = sort_values_with_nan(movements)
movements.insert(0, "All values")
st.sidebar.markdown("**Movement**")
selected_movement = st.sidebar.selectbox("", options=movements)
if selected_movement != "All values":
    filtered_df = filtered_df[filtered_df["Movement"] == selected_movement]

# Production year filter (dropdown)
if "Year of production" in filtered_df.columns and not filtered_df["Year of production"].isna().all():
    years = sort_values_with_nan(sorted(filtered_df["Year of production"].dropna().unique().tolist()))
    years.insert(0, "All values")
    st.sidebar.markdown("**Year of production**")
    selected_year = st.sidebar.selectbox("", options=years)
    if selected_year != "All values":
        filtered_df = filtered_df[filtered_df["Year of production"] == selected_year]

# Location filter (dropdown)
locations = filtered_df["Location"].unique().tolist()
locations = sort_values_with_nan(locations)
locations.insert(0, "All values")
st.sidebar.markdown("**Location**")
selected_location = st.sidebar.selectbox("", options=locations)
if selected_location != "All values":
    filtered_df = filtered_df[filtered_df["Location"] == selected_location]

# Check if the filtered DataFrame is empty
if filtered_df.empty:
    st.write("No results found.")
else:
    # Top row: two pie charts
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 🥧 Distribution of Brands")
        brand_counts = filtered_df['Brand'].value_counts()

        brand_fig = go.Figure(data=[go.Pie(
            labels=marca_counts.index,
            values=marca_counts.values,
            hole=0.4,
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']),
            textinfo='label+percent',
            insidetextorientation='radial'
        )])
        brand_fig.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            showlegend=True,
            paper_bgcolor="#ffffff",
            font=dict(color="#262626")
        )
        st.plotly_chart(brand_fig, use_container_width=True)

    with col2:
        st.write("### 🥧 Distribution by Movement types")
        movement_counts = filtered_df['Movement'].value_counts()

        movement_fig = go.Figure(data=[go.Pie(
            labels=movement_counts.index,
            values=movement_counts.values,
            hole=0.4,
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880']),
            textinfo='label+percent',
            insidetextorientation='radial'
        )])
        movement_fig.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            showlegend=True,
            paper_bgcolor="#ffffff",
            font=dict(color="#262626")
        )
        st.plotly_chart(movement_fig, use_container_width=True)

    # Bottom row: bar chart across full width
    col3 = st.container()

# Bottom row: 2 columns (Date chart + ChatGPT box)
    col3, col4 = st.columns(2)

    with col3:
        st.write("### 📊 Distribution by Date")
        filtered_df["date"] = pd.to_datetime(filtered_df["date"], errors="coerce")
        date_counts = filtered_df["date"].dt.date.value_counts().sort_index()

        date_fig = go.Figure([go.Bar(
            x=date_counts.index.astype(str),
            y=date_counts.values,
            marker_color='#262626'
        )])
        date_fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Number of Advertisements",
            height=400,
            margin=dict(l=20, r=20, t=40, b=60),
            xaxis_tickangle=-45,
            plot_bgcolor="#ffffff",
            paper_bgcolor="#ffffff",
            font=dict(color="#262626"),
            xaxis=dict(type='category')
        )
        st.plotly_chart(date_fig, use_container_width=True)

    with col4:
        st.write("### 💬 Ask about the data")
        
        # Display a fake chat box and respond
        user_input = st.chat_input("Ask me a question about the data...")
        if user_input:
            # Dummy response for now; you can replace this with actual logic
            st.write(f"**You asked:** {user_input}")
            # Here you could add logic like keyword-based answers or use LangChain/OpenAI if external integration is possible
            st.write("🔍 (Pretending to analyze data...)")
            st.write("📈 I'm just a placeholder! But in a real app, I could tell you insights from your data.")





