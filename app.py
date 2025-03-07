import streamlit as st

st.set_page_config( layout="wide", page_title="Watch Metrics",page_icon="📊")

# Apply custom CSS to change the sidebar background color to white
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: White !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

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

#st.sidebar.markdown("Made with ❤️ by [Goldhandfinance](https://youtube.com/@goldhandfinance)")

# --- STOCK ---
watch_data = st.Page(
    "views/watch_data.py",
    title="Data",
    icon=":material/bar_chart:",
)

watch_plot = st.Page(
    "views/watch_plot.py",
    title="Plot",
    icon=":material/bar_chart:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

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
    #link="https://goldhandfinance.streamlit.app/",
    size="large")

# --- RUN NAVIGATION ---
pg.run()
