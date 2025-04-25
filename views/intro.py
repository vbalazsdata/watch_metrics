import streamlit as st

# Main Title
@st.fragment
def intro():
    st.title("⏱️ Watch Metrics")

    # Introduction Text
    st.markdown(
        """
         
        xxxxxxThis project was born out of my passion for **data analysis** and **watch collecting**.  
        The goal is to help me **analyze and foresee market trends** 🔎, while also making it easier to  
        **rationalize and reorganize my watch collection** whenever I feel like it.  

        💡 **A Personal Project**  
        This app is just for me—I don’t plan to share it with a wider audience or make any money from it.  
        It’s simply a tool to enhance my understanding of the market and optimize my collection.  

        🚀 **What’s Next?**  
        Many more features will be added over time! As I gain more knowledge in **Python** 🐍  
        and as time allows, I'll continue to develop and refine this app.  

        Stay tuned for more updates!
        """,
        unsafe_allow_html=True
    )

intro()
