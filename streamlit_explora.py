### Streamlit app for interactive exploration ###

##imports##
import streamlit as st

# Frontend using streamlit"
import streamlit as st
import requests
import json

from st_synthesis import run_synthesis
from st_statistical_analysis import run_statistical_analysis
from st_ai_model import run_ai_model
from st_about import run_about

st.set_page_config(page_title="Explora: AI Explainability", layout="wide")
        
def run():
    
    st.title("Explora AI Explainability")

    menu = ["About",
            "Synthesis", 
            "Statistical Analysis",
            "ML Modeling" 
            ]

    choice = st.sidebar.radio("Menu", menu)
    if choice == "Synthesis":
        st.subheader("Synthesis:")
        run_synthesis()
    elif choice == "Statistical Analysis":
        st.subheader("Statistical Analysis")
        run_statistical_analysis()
    elif choice == "ML Modeling":
        st.subheader("ML Modeling:")
        run_ai_model()
    else:
        st.subheader("About:")
        run_about()
        

           
    
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()

