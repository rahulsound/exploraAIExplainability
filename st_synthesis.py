import streamlit as st


def run_synthesis():
    #run_synthesis
    st.header("This pages lists several observations in Q'nA format:")

    st.divider()

    st.subheader("Question: Are there any favourite states for the agent?")
    st.divider()

    st.markdown(''':blue[**1. Visualize the state-transition graph where the node-size is proportional to number of edges:**] ''')
    st.image('nodes_and_edges.png')
    st.write('**Observations:**')
    st.write('- Agent  embb-trf1 has one repeated state whereas urllc-trf2 has several recurrin states')
    st.write('- This is not conclusive but it does seem the agent transitions to a few selected states repeatedly.')
    st.divider()

    st.markdown(''' :blue[**2. Visualize the count of transitions split into "FROM" and "TO" to see if there is a pattern**] ''')
    st.image('from_to_counts-urllctrf1.png')
    st.write('**Observations:**')
    st.write('- A state like: (12,15,23,1,2,0) has “from_count” = 15 and “to_count”=6 i.e “from_count” > “to_count ')
    st.write('- This might imply  this state may be the starting state (default) for several UEs within Exp#30 ')
    
    st.write(' - From and To view of all agents:')
    st.image('from_to_counts_all.png')
    st.divider()

    st.subheader("Question: What are the true implications of a repeating transition? How does it impact KPI?")

    st.divider()

    st.markdown(''' :blue[**1. Using the \"repeat-transition\" samples, compute a new KPI to analyze the impact:**] ''')
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
    st.markdown(''':blue[**2. Plot the variance of new KPIs for transitions that repeat once or twice to see if the 'repeats' a relationship with variance:**] ''')
    st.image('variance_repeats.png')
    st.write("**Observations:**")
    md = ('''
            - Since there are very few samples with 3 or more transitions, the above split is based on non-repeating transitions (right) v/s repeating transitions (left)
            - There is no clear evidence of change in variance due to repeated transitions
            - This may imply that even though the agent has a 'favourite transition', it doesn't imply it results in a better KPI
            - The same is confirmed by the box plot below.
          ''')
    st.write(md)
    st.image('variance_repeats_box.png')
    st.divider()

    st.subheader("Question: What is the implication of a repeating transition for an agent? Do some slices benefit in KPI by going to a 'favourite state'?")


    st.markdown(''':blue[**1. Plot the variance of new KPIs for transitions that repeat once/twice/thrice/four times for each slice for URLLC-TRF1 as an example:**] ''')
    st.write('Agent: URLLC-TRF1, Slice: 0')
    st.image('mean_delta_utrf-slice0.png')
    st.write('Agent: URLLC-TRF1, Slice: 1')
    st.image('mean_delta_utrf-slice1.png')
    st.write('Agent: URLLC-TRF1, Slice: 2')
    st.image('mean_delta_utrf-slice2.png')

    st.write("**Observations:**")
    md = ('''
            - For slice_1 and slice_2, some predictability is possible (linear regression line) but not for slice_0
        ''')
    st.write(md)

    st.divider()