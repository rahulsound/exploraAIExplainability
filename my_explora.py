import streamlit as st
from my_startup import run_startup
from my_interests import run_interests
from my_about import run_about

def run_explora():

    md = ('''
            - Exploring graph-based methods for AI explainability with senior researchers: [Michele Polese](https://scholar.google.it/citations?user=JmMEy-QAAAAJ&hl=en) from [Northeastern University](https://www.northeastern.edu/) & [Dr. Claudio
            Fiandrino](https://scholar.google.com/citations?user=sxt0fiYAAAAJ&hl=it) from [IMDEA Networks](https://networks.imdea.org/). 
            - Project Details:
                -   [EXPLORA](https://dl.acm.org/doi/10.1145/3629141) : AI/ML EXPLainability for the Open RAN. Use case: Slicing and scheduling [ [Paper](https://dl.acm.org/doi/10.1145/3629141) | [GitHub](https://github.com/wineslab/explora) ]
                -   Tech Stack: Reinforcement Learning, O-RAN RIC (use case: network slicing), AI/ML Explainability, Python, numpy, sklearn, matplotlib. 
                -   Endorsements: [ [Dr. Claudio Fiandrino](https://www.linkedin.com/in/rahul-soundrarajan/overlay/experience/2308452531/multiple-media-viewer?profileId=ACoAAAEghN0BEVHghG1jkZJUhaxlFQ8oxPDexlM&treasuryMediaId=1713929436419&type=DOCUMENT&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3B2KyN%2BdqnR2irI5xRESearg%3D%3D) | [Michele Polese](https://www.linkedin.com/in/rahul-soundrarajan/overlay/experience/2308452531/multiple-media-viewer?profileId=ACoAAAEghN0BEVHghG1jkZJUhaxlFQ8oxPDexlM&treasuryMediaId=1713929436418&type=DOCUMENT&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BK5baOBvHSRuNqMwA788cPA%3D%3D) ]
          ''')
    st.write(md)

    st.divider()
    st.subheader(''':red[Link to ongoing analysis with visualizations: [here](https://explora-ai-explainability.streamlit.app/)] ''')
