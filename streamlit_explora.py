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
from st_play_with_data import run_play_with_data

st.set_page_config(page_title="Explora: AI Explainability", layout="wide")
        
def run():
    
    st.title("EXPLORA")
    st.subheader("AI/ML EXplainability for O-RAN - A deeper analysis:")
    st.divider()

    menu = ["About",
            "Synthesis", 
            "Statistical Analysis",
            "ML Modeling",
            "Play with data" 
            ]

    choice = st.sidebar.radio("Menu", menu)
    if choice == "Synthesis":
        #st.subheader("Synthesis:")
        #st.divider()
        st.write(":blue[This page attempts to synthesise the available data in Q'nA format to help guide the interpretations... ]")
        st.divider()
        run_synthesis()
    elif choice == "Statistical Analysis":
        #st.subheader("Statistical Analysis:")
        #st.divider()
        st.write(":blue[This page attempts to perform statsitical analysis on the available data in Q'nA format to help guide various aspects related to data [distribution, sufficiency, etc.].] ")
        st.divider()
        run_statistical_analysis()
    elif choice == "ML Modeling":
        #st.subheader("ML Modeling:")
        #st.divider()
        st.write(":blue[This page attempts to guide ML model development in Q'nA format to help guide the model building and subsquent interpretations...] ")
        st.divider()
        run_ai_model()
    elif choice == "Play with data":
        #st.subheader("ML Modeling:")
        #st.divider()
        st.write(":blue[This page provides an interactive way of exploring the data] ")
        st.divider()
        run_play_with_data()
    else:
        #st.subheader("About:")
        run_about()
        

           
    
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()

