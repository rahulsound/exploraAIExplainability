

##imports##
import streamlit as st

# Frontend using streamlit"
import streamlit as st
import requests
import json
import os

from my_projects import run_projects
from my_papers import run_papers
from my_home import run_home
from my_startup import run_startup
import streamlit_option_menu

st.set_page_config(page_title="Rahul Soundrarajan", layout="wide")
from streamlit_option_menu import option_menu
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)




def run_contact():
    with st.container():
        st.write("---")
        st.header("Get In Touch!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/rahulsound@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

        
def run():
    
    st.header("Rahul Soundrarajan")
    
    def streamlit_menu():
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Start-up", "Projects", "Research Papers", "Contact"],  # required
            icons=["house", "asterisk", "book", "mortarboard", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected


    selected = streamlit_menu()

    if selected == "Home":
        run_home()
    elif selected == "Projects":
        run_projects()
    elif selected == "Research Papers":
        run_papers()
    elif selected == "Contact":
        run_contact()
    elif selected == 'Start-up':
        run_startup()

# selected_page = option_menu(None, pagelist, icons=pageicons, default_index=page, key="page", on_change=update_query_params)       
    
if __name__ == '__main__':
    #by default it will run at 8501 port
    local_css(os.getcwd() + os.path.sep +  'style' + os.path.sep + 'style.css')
    run()

