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
        A **Streamlit-based interactive analysis platform** where you can visualize 📊, filter 🔍, and analyze 📈 a vast amount of watch data!
        
        🎯 **What can you do here?**  
        - 📥 Download the latest watch data  
        - 🔎 Perform detailed analyses on prices and trends  
        - 📊 Easily overview market movements with interactive charts  

        🚀 **Why is this useful for you?**  
        - If you're a watch collector, it helps you find the best deals ⏳💎  
        - If you're a trader, you can make better decisions based on market analysis 📈💰  
        - If you simply love watches, you can discover tons of interesting insights 🧐
        - Or just get some ideas if you want to reorganize your collection ☝️

        🤩 Get started now and explore the world of watches from a new perspective!
        """,
        unsafe_allow_html=True
    )

about()
