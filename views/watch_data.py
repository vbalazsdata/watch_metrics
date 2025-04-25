import pandas as pd
import streamlit as st
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
st.title("Data explorer")

# Creating a copy of the DataFrame for filtering
filtered_df = df.copy()

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
movements = filtered_df["Caliber/movement"].unique().tolist()
movements = sort_values_with_nan(movements)
movements.insert(0, "All values")
st.sidebar.markdown("**Caliber/movement**")
selected_movement = st.sidebar.selectbox("", options=movements)
if selected_movement != "All values":
    filtered_df = filtered_df[filtered_df["Caliber/movement"] == selected_movement]

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

# Check if there are any data after filtering
if filtered_df.empty:
    st.write("No results found.")
else:
    # Description of the page
    #st.markdown("## Explore the raw dataset in details")
    st.markdown("### Use filters and sorting to dive into individual records, spot patterns, or verify specific entries.")
    st.markdown("*** You can always see 100 rows in this table due to performance reasons. Try to narrow down yuour search as much as possible! ***")    
    st.markdown("---")
    
    # Format the results in markdown with HTML and CSS
    st.markdown("### Latest Update")
    st.markdown(
        f"""
        <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Latest Update: 🔄 {latest_update}</h3>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Create a grid with 3 smaller tiles below the latest update
    st.markdown(
        f"""
        <div style="display: flex; justify-content: space-between; margin-top: 20px;">
            <div style="background-color: #e0f7fa; padding: 15px; border-radius: 10px; width: 30%; text-align: center;">
                <h4>Number of Records for Latest Date</h4>
                <p>{num_latest}</p>
            </div>
            <div style="background-color: #ffe0b2; padding: 15px; border-radius: 10px; width: 30%; text-align: center;">
                <h4>Nominal Difference</h4>
                <p>{nominal_diff}</p>
            </div>
            <div style="background-color: #c8e6c9; padding: 15px; border-radius: 10px; width: 30%; text-align: center;">
                <h4>Percentage Difference</h4>
                <p>{percentage_diff:.2f}%</p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.dataframe(filtered_df.head(100))


