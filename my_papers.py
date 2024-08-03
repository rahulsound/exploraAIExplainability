import streamlit as st
from paper_rl_near_rt import run_rl_near_rt_ric

def run_papers():
    menu = ["RL in Near-RT RIC",
            "Null"
            ]

    choice = st.sidebar.radio("Menu", menu)
    if choice == "RL in Near-RT RIC":
        run_rl_near_rt_ric()


    st.divider()