import streamlit as st

# Main Title
@st.fragment
def intro():
    st.title("⏱️ Watch Metrics")

    # Introduction Text
    st.markdown(
        """
         
        This project was born out of my passion for **data analysis** and **watch collecting**.
        The goal is to help me **analyze and foresee market trends** 🔎, while also making it easier to
        **rationalize and reorganize my watch collection** whenever I feel like it.

        💡 **A Personal Project**              
        This is simply a tool for me to enhance my understanding of the market and optimize my collection.
        Also, I wanted to learn **Python** 🐍 and **Streamlit** 📊, so I decided to create this app as a final assignment for a Python course.

        🚀 **What’s Next?**
        This is just the beginning! As I continue learning Python and find more time, I'll keep expanding and improving this app.

        ***Stay tuned for more updates!***
        """,
        unsafe_allow_html=True
    )

intro()
