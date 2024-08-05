import streamlit as st


def run_about():
    #Run Deep Dives Analysis
    st.write("Research and Analysis compiled by [Rahul Soundrarajan](https://rahulsound.streamlit.app/) using [Streamlit](https://streamlit.io/)" )

    st.divider()

    st.markdown('#### The deep-dive presented here is based on the Explora Project: https://github.com/wineslab/explora')
    md = (''' 
          EXPLORA: AI/ML EXPLainability for the Open RAN
          Claudio Fiandrino, Leonardo Bonati, Salvatore d'Oro, Michele Polese, Tommaso Melodia, Joerg Widmer
          CoNEXT ’23, December 5–8, 2023, Paris, France
          DOI: 10.1145/3629141
          ''')
    st.text(md)

    st.divider()
    st.subheader('The objective of this analysis is to focus on:')
    md = ('''
          1. Improvement of the capabilities of the basic EXPLORA framework toward a refined synthesis of explanations concerning the operation of a deep reinforcement learning (DRL) agent; in more details, modify the basic operation that synthesizes explanations departing from a knowledge graph by taking into consideration the importance of the edges
          2. Perform an in-depth statistical analysis to quantify in more details the effect of the actions of the DRL agent on the networks state
          3. Based on the above points, develop a new AI model that makes it possible to predict the effect the actions with statistical confidence.
            '''
          )
    st.write(md)

    st.divider()

    st.write("The deep-dive presented in this analysis relates specifically to the Fig:12 from the paper shown below:")
    st.image("explora_fig_12.png")
    st.divider()

    st.write('The process of building this attributed graph is shown in the figure below:')
    st.image("explora_fig_11.png")
    st.divider()

    st.markdown('''#### :blue[ Please click through the menu on the left for a deep dive] ''')
    st.divider()
