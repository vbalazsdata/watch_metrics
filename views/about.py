import streamlit as st

# Main Title
@st.fragment
def about():
    st.title("⏱️ Watch Metrics")

    # Introduction Text
    st.markdown(
        """
        ## Welcome to the **Watch Metrics** App!
        
        📌 **What is this app?**  
        A **Streamlit-based interactive analysis platform** where you can analyze 📈 a vast amount of watch data.<br><br>
        The data is sourced from one of the big watch portals and includes a wide range of watch brands and models.
        
        🎯 **What can you do here?**  
        - 📥 Download watch related data
        - 🔎 Perform detailed analyses on prices and trends
        - 📊 Easily overview market movements with interactive charts

        🚀 **Why is this useful for you?**  
        - If you're a trader, you can make better decisions based on market analysis 📈💰  
        - If you simply love watches, you can discover tons of interesting insights 🧐
        - Or just get some ideas if you want to reorganize your collection ☝️

        🚀 Let’s explore and find out what the market has to say!
        """,
        unsafe_allow_html=True
    )

about()
