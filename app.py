import streamlit as st

st.set_page_config( layout="wide", page_title="Watch Metrics",page_icon="📊")

# --- INTRO ---
about_page = st.Page(
    "views/about.py",
    title="About this app",
    icon=":material/account_circle:",
    default=True,
)

intro_page = st.Page(
    "views/intro.py",
    title="Introduction",
    icon=":material/account_circle:",
    
)


# --- STOCK ---
watch_data = st.Page(
    "views/watch_data.py",
    title="Data explorer",
    icon=":material/bar_chart:",
)

watch_plot = st.Page(
    "views/watch_plot.py",
    title="Insights",
    icon=":material/bar_chart:",
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page, intro_page],
        "Analysis": [watch_data, watch_plot],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo(
    'https://i.ibb.co/fd47vzPJ/logo.png',
    size="large")

# --- RUN NAVIGATION ---
pg.run()
