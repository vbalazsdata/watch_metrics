import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px  # For the treemap chart
from utils import get_data

# Loading data
df = get_data()

# Calculating dates
latest_update = df['date'].max()
second_latest_update = df['date'][df['date'] < latest_update].max()

# Calculating number of ads
num_latest = df[df['date'] == latest_update].shape[0]
num_second_latest = df[df['date'] == second_latest_update].shape[0]

# Calculate the nominal difference and percentage difference
nominal_diff = num_latest - num_second_latest
percentage_diff = (nominal_diff / num_second_latest * 100) if num_second_latest != 0 else 0

# Page title
st.title("Metrics Overview")

# Description of the page
st.markdown("## Visualize your data insights through interactive charts")
st.markdown("Explore trends, correlations, and patterns with dynamic graphs to make data analysis easier and more intuitive.")
st.markdown("---") 

# Format the results in markdown with HTML and CSS for the latest update
st.markdown(
    f"""
    <div style="background-color: #778da9; color: #ffffff; padding: 15; border-radius: 10px; text-align: center;">
        <h3>🔄 Latest Update: {latest_update}</h3>
    </div>
    """, 
    unsafe_allow_html=True
)

# Create a grid with 3 smaller tiles below the latest update
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; margin-top: 20px;">
        <div style="background-color: #1b263b; color: #ffffff; padding: 10; border-radius: 10px; width: 30%; text-align: center;">
            <h4>{num_latest}</h4>
            <p>Ads in the latest dataset</p>
        </div>
        <div style="background-color: #1b263b; color: #ffffff; padding: 10; border-radius: 10px; width: 30%; text-align: center;">
            <h4>{nominal_diff}</h4>
            <p>Ads since the previous update</p>
        </div>
        <div style="background-color: #1b263b; color: #ffffff; padding: 10; border-radius: 10px; width: 30%; text-align: center;">
            <h4>{percentage_diff:.2f}%</h4>
            <p>Market growth (in number of ads)</p>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

# Sidebar filters
st.sidebar.header("🔍 Filters")

def sort_values_with_nan(values):
    sorted_values = sorted([v for v in values if pd.notna(v)]) + [v for v in values if pd.isna(v)]
    return sorted_values

# Brand filter (dropdown)
brands = df["Brand"].unique().tolist()
brands = sort_values_with_nan(brands)
brands.insert(0, "All values")
st.sidebar.markdown("**Brand**")
selected_brand = st.sidebar.selectbox("", options=brands)
if selected_brand != "All values":
    df = df[df["Brand"] == selected_brand]

# Model filter (dropdown)
models = df["Model"].unique().tolist()
models = sort_values_with_nan(models)
models.insert(0, "All values")
st.sidebar.markdown("**Model**")
selected_model = st.sidebar.selectbox("", options=models)
if selected_model != "All values":
    df = df[df["Model"] == selected_model]

# Movement filter (dropdown)
movements = df["Caliber/movement"].unique().tolist()
movements = sort_values_with_nan(movements)
movements.insert(0, "All values")
st.sidebar.markdown("**Caliber/movement**")
selected_movement = st.sidebar.selectbox("", options=movements)
if selected_movement != "All values":
    df = df[df["Caliber/movement"] == selected_movement]

# Production year filter (dropdown)
if "Year of production" in df.columns and not df["Year of production"].isna().all():
    years = sort_values_with_nan(sorted(df["Year of production"].dropna().unique().tolist()))
    years.insert(0, "All values")
    st.sidebar.markdown("**Year of production**")
    selected_year = st.sidebar.selectbox("", options=years)
    if selected_year != "All values":
        df = df[df["Year of production"] == selected_year]

# Location filter (dropdown)
locations = df["Location"].unique().tolist()
locations = sort_values_with_nan(locations)
locations.insert(0, "All values")
st.sidebar.markdown("**Location**")
selected_location = st.sidebar.selectbox("", options=locations)
if selected_location != "All values":
    df = df[df["Location"] == selected_location]

# Date filter (dropdown)
dates = sorted(df['date'].unique())
dates.insert(0, "All values")
st.sidebar.markdown("**Date**")
selected_date = st.sidebar.selectbox("Select a date", options=dates)
if selected_date != "All values":
    df = df[df["date"] == selected_date]

st.sidebar.markdown("---")

# Create the layout grid for charts and dummy text
col1, col2, col3 = st.columns(3)

# First row: Treemap of Brands, dummy text, Treemap of Movement types, dummy text
with col1:
    st.write("### ⌚ Distribution of Brands")
    # Calculate Brand Distribution
    brand_counts = df['Brand'].value_counts().reset_index()
    brand_counts.columns = ['Brand', 'Count']  # Rename columns for clarity

    # Create Treemap for Brand Distribution
    brand_fig = px.treemap(brand_counts, 
                        path=['Brand'], 
                        values='Count', 
                        color='Count', 
                        hover_data=['Brand'],
                        title="Distribution of Brands")
    st.plotly_chart(brand_fig, use_container_width=True)

with col2:
    st.write("### ⚙️ Distribution of Movement Types")
    # Calculate Movement Distribution
    movement_counts = df['Movement'].value_counts().reset_index()
    movement_counts.columns = ['Movement', 'Count']  # Rename columns for clarity

    # Create Treemap for Movement Distribution
    movement_fig = px.treemap(movement_counts, 
                            path=['Movement'], 
                            values='Count', 
                            color='Count', 
                            hover_data=['Movement'],
                            title="Distribution of Movement Types")
    st.plotly_chart(movement_fig, use_container_width=True)

with col3:
    st.write("### 📊 Distribution by Date")
    filtered_df = df.copy()
    filtered_df["date"] = pd.to_datetime(filtered_df["date"], errors="coerce")
    date_counts = filtered_df["date"].dt.date.value_counts().sort_index()

    date_fig = go.Figure([go.Bar(
        x=date_counts.index.astype(str),
        y=date_counts.values,
        #marker_color='#262626'
    )])
    date_fig.update_layout(
        #xaxis_title="",
        yaxis_title="Number of Advertisements",
        height=400,
        margin=dict(l=20, r=20, t=40, b=60),
        xaxis_tickangle=-45,
        #plot_bgcolor="#ffffff",
        #paper_bgcolor="#ffffff",
        #font=dict(color="#262626"),
        #xaxis=dict(type='category')
    )
    st.plotly_chart(date_fig, use_container_width=True)    


# Second row: Bar chart for Date distribution, dummy text, Chatbox
col4 = st.columns(1)



with col4:
    st.write("Some dummy text here. This section can be used for providing additional insights or context about the bar chart above.")


    # Display a chatbox for user input
    user_input = st.chat_input("Ask me a question about the data...")
    if user_input:
        # Dummy response for now; you can replace this with actual logic
        st.write(f"**You asked:** {user_input}")
        # Here you could add logic like keyword-based answers or use LangChain/OpenAI if external integration is possible
        st.write("🔍 (Pretending to analyze data...)")
        st.write("📈 I'm just a placeholder! But in a real app, I could tell you insights from your data.")
