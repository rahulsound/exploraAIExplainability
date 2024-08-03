import streamlit as st
from my_patents import run_patents
from my_skills_and_interests import run_skills_and_interests
from my_about import run_about


def run_home():
    menu = ["About",
            "Patents", 
            "Skills and Interests" 
            ]

    choice = st.sidebar.radio("Menu", menu)
    if choice == "About":
        run_about()
    elif choice == "Patents":
        run_patents()
    elif choice == "Skills and Interests":
        run_skills_and_interests()

    st.divider()
