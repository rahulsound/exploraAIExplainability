import streamlit as st
from my_patents import run_patents
from my_skills_and_interests import run_skills_and_interests



def run_about():

    st.subheader('Summary:')
    md = ('''
        With over 23 years of diverse experience in telecom, machine learning, sensor fusion, and computer vision, I am an AI/ML technical consultant who designs and implements custom solutions for challenging problems that require cutting-edge technologies and deep domain knowledge.

        I hold multiple patents and publications in applied ML, specifically related to network optimization. In my previous role, I have designed and evaluated complex ML based solutions for O-RAN (Near and Non-RT RAN Intelligent Controller)

        Currently, I am working with Northeastern University and IMDEA Networks on EXPLORA, a framework that provides explainability of DRL-based control solutions for the Open RAN ecosystem.

        In my last role, as a founding member and VP of ML & SW Engineering at BlueFusion Inc., a Boston based start-up, I designed ML-based sensor fusion algorithms that helped demonstrate the capability and promise of the solution. This solution has applications for automotive, surveillance, UAVs, smart homes, V2X, and factory automation, and was in the start-up inception programs of Microsoft and Nvidia.

        I am passionate about creating innovative and impactful solutions that leverage the power of AI/ML and edge computing. 
        '''
          )
    st.write(md)
    st.divider()
