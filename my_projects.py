import streamlit as st
from my_startup import run_startup
from my_interests import run_interests
from my_about import run_about
from my_explora import run_explora
from my_papers import run_papers
from my_ml_ran_projects import run_ml_ran_projects

def run_projects():
    menu = [
            "Explora", 
            "ML in RAN" 
            ]

    choice = st.sidebar.radio("Menu", menu)
    if choice == "Explora":
        st.subheader('Technical Consultant | AI/ML - O-RAN | Dec-1 2023 - Present ')
        run_explora()
    elif choice == "ML in RAN":
        run_ml_ran_projects()

    st.divider()