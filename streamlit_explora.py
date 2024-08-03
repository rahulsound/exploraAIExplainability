### Streamlit app for interactive exploration ###

##imports##
import streamlit as st

# Frontend using streamlit"
import streamlit as st
import requests
import json

from st_static import run_static_analysis
from st_deep_div import run_deep_dive

        
def run():
    
    st.title("Explora AI Explainability")

    menu = ["Static Analysis", 
            "Deep Dive", 
            "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Static Analysis":
        st.header("Static Analysis Menu")
        run_static_analysis()
    elif choice == "Deep Dive":
        st.header("Deep Dive Menu")
        run_deep_dive()
    else:
        st.header("About")

           
    
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()

