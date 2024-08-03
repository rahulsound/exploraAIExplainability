import streamlit as st


def run_synthesis():
    #run_synthesis
    st.header("This pages lists several observations in Q'nA format:")

    st.divider()

    st.subheader("Question: Are there any favourite states for the agent?")
    st.divider()

    st.write("1. Visualize the state-transition graph where the node-size is proportional to number of edges:")
    st.image('nodes_and_edges.png')
    st.write('**Observations:**')
    st.write('- Agent  embb-trf1 has one repeated state whereas urllc-trf2 has several recurrin states')
    st.write('- This is not conclusive but it does seem the agent transitions to a few selected states repeatedly.')
    st.divider()

    st.write('2. Visualize the count of transitions split into "FROM" and "TO" to see if there is a pattern')
    st.image('from_to_counts-urllctrf1.png')
    st.write('**Observations:**')
    st.write('- A state like: (12,15,23,1,2,0) has “from_count” = 15 and “to_count”=6 i.e “from_count” > “to_count ')
    st.write('- This might imply  this state may be the starting state (default) for several UEs within Exp#30 ')
    
    st.write(' - From and To view of all agents:')
    st.image('from_to_counts_all.png')
    st.divider()

    st.subheader("Question: What are the true implications of a repeating transition? How does it impact KPI?")

    st.divider()

    st.write("Using the \"repeat-transition\" samples, compute a new KPI to analyze the impact:")
    st.image('custom_kpi.png')
    st.write("**Observations:**")
    md = ('''
            - Analysis of repeating transitions (To-From combination such as: “[' 6', ' 9', ' 35', ' 1', ' 1', ' 0', ' 6', ' 9', ' 35', ' 0', ' 1', ' 0']”)
            - These observations are made using the sl0_df, sl1_df, sl2_df available here: https://github.com/wineslab/explora/blob/main/scripts/analysis-explora.py#L949 
            - For repeating transitions, the metrics such as sl0_mean_tx_brate shown below is computed by doing a groupby(transition)[‘tx_brate’].agg(‘mean’) operation. It needs to be confirmed if it reflects a useful metric. It can be see that there is big variation in mean values across slices. The below table is for urllc-trf1
            - Observations:
                -   All 3 dataframes (sl0_df, sl1_df, sl2_df) have the same list of transitions, the metrics differ due to slice
                -   A few transitions have identical “To” and “From” states, highlighted below in green
          ''')
    st.write(md)
    st.divider()

    