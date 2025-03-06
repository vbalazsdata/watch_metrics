import pandas as pd
import streamlit as st
from utils import get_data

# Adatok betöltése
df = get_data()

# Oldalcím
#st.title("⏱️ Watch Metrics")

# Másolat a DataFrame-ből, amit szűrni fogunk
filtered_df = df.copy()

# Szűrők beállítása - Sidebar háttérszín
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #ADD8E6;
        }
        /* Style the selectbox to have a mid-blue background and white text */
        .css-1wa3eu0, .css-1wa3eu0:hover, .css-1wa3eu0:focus {
            background-color: #4682B4; /* Mid blue background */
            color: white; /* White text */
        }
        /* Ensuring the input text inside the selectbox is white */
        .css-1wa3eu0 input {
            color: white;
        }
        /* Customizing the dropdown arrow color */
        .css-1wa3eu0 .css-1e9m5g5 {
            color: white;
        }
        /* Adjust the hover state for the dropdown options */
        .css-1wa3eu0 .css-1v0mbdj:hover {
            background-color: #5A9BD5; /* Slightly lighter blue on hover */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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
movements = filtered_df["Caliber/movement"].unique().tolist()
movements = sort_values_with_nan(movements)
movements.insert(0, "All values")
st.sidebar.markdown("**Caliber/movement**")
selected_movement = st.sidebar.selectbox("", options=movements)
if selected_movement != "All values":
    filtered_df = filtered_df[filtered_df["Caliber/movement"] == selected_movement]

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
    # Szűrt táblázat megjelenítése
    #st.write("📊 Showing the filtered table:")
    st.dataframe(filtered_df)
