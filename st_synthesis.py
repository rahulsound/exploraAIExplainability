import streamlit as st


def run_synthesis():
    #run_synthesis
    st.header("This pages lists several observations in Q'nA format:")

    st.divider()

    st.subheader("Question: Are there any favourite states for the agent?")
    st.write("Visualize the state-transition graph where the node-size is proportional to number of edges:")
    st.image('nodes_and_edges.png')
    st.write('**Observations:**')
    st.write('- Agent  embb-trf1 has one repeated state whereas urllc-trf2 has several recurrin states')
    st.write('- This is not conclusive but it does seem the agent transitions to a few selected states repeatedly.')
    st.divider()

    st.write('Visualize the count of transitions split into "FROM" and "TO" to see if there is a pattern')
    st.image('from_to_counts.png')
    st.write('**Observations:**')
    st.write('- A state like: (12,15,23,1,2,0) has “from_count” = 15 and “to_count”=6 i.e “from_count” > “to_count ')
    st.write('- This might imply  this state may be the starting state (default) for several UEs within Exp#30 ')
    st.divider()