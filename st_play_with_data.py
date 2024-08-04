import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def run_play_with_data():
    #Run Static Analysis
    st.subheader("")
    combo = pd.read_csv('combo.csv')
    c1 = combo[[ 'count_norm', 'tx_brate_norm', 'tx_pkts_norm', 'dl_buffer_norm', 'slice', 'agent']]
    dfx = c1['agent'].value_counts()
    st.subheader('Count of samples per agent: ')
    st.bar_chart(dfx, width=400)
    st.divider()

    st.subheader("Correlation Analysis of 2 variables")
    st.code(''' 
            #Description of columns:
            'count_norm': count of repeats of a particular state [2 means the state has repeated twice]
            '{kpi}_norm': normalized value of the KPIs: 'tx_brate', 'tx_pkts', 'dl_buffer'
            'slice'     : slice IDs: [0,1,2]
            'agent'     : agents: ['embb-trf1', 'embb-trf2', 'urllc-trf1', 'urllc-trf1'  ]
            ''', language='python') 
    feature_x = st.selectbox('Select feature for x axis', c1.columns)
    feature_y = st.selectbox('Select feature for y axis', c1.columns)   

    fig, ax = plt.subplots()
    sns.scatterplot(data=c1, x=feature_x, y=feature_y, ax=ax)
    st.pyplot(fig)
    st.divider()

    st.subheader("Plot of Distribution of KPIs per agent OR per slice")
    st.code(''' 
            #Description of columns:
            'count_norm': count of repeats of a particular state [2 means the state has repeated twice]
            '{kpi}_norm': normalized value of the KPIs: 'tx_brate', 'tx_pkts', 'dl_buffer'
            'slice'     : slice IDs: [0,1,2]
            'agent'     : agents: ['embb-trf1', 'embb-trf2', 'urllc-trf1', 'urllc-trf1'  ]
            ''', language='python') 
    

    feature_x = st.selectbox('Select KPI', ['tx_brate_norm', 'tx_pkts_norm', 'dl_buffer_norm'])
    feature_y = st.selectbox('Select Split-by cretieron: ', ['slice', 'agent'])

    distplot = sns.displot(data=c1, x=feature_x, hue=feature_y, kind="kde")
    st.pyplot(distplot.fig)
    st.divider()  

    st.subheader("Plot of Distribution of KPIs per agent OR per slice  | side-by-side view:")
    st.code(''' 
            #Description of columns:
            'count_norm': count of repeats of a particular state [2 means the state has repeated twice]
            '{kpi}_norm': normalized value of the KPIs: 'tx_brate', 'tx_pkts', 'dl_buffer'
            'slice'     : slice IDs: [0,1,2]
            'agent'     : agents: ['embb-trf1', 'embb-trf2', 'urllc-trf1', 'urllc-trf1'  ]
            ''', language='python') 
    

    feature_x1 = st.selectbox('Select KPI for plot', ['tx_brate_norm', 'tx_pkts_norm', 'dl_buffer_norm'])
    feature_y1 = st.selectbox('Select Split-by cretieron: for plot', ['slice', 'agent'])
    if feature_y1 == 'slice':
        col = 'agent'
    else:
        col = 'slice'


    distplot1 = sns.displot(data=c1, x=feature_x1, hue=feature_y1, col=col, kind="kde")
    st.pyplot(distplot1.fig)
    st.divider()   

    # st.subheader("KDE Plot of Distribution of KPIs per agent OR per slice")
    # st.code(''' 
    #         #Description of columns:
    #         'count_norm': count of repeats of a particular state [2 means the state has repeated twice]
    #         '{kpi}_norm': normalized value of the KPIs: 'tx_brate', 'tx_pkts', 'dl_buffer'
    #         'slice'     : slice IDs: [0,1,2]
    #         'agent'     : agents: ['embb-trf1', 'embb-trf2', 'urllc-trf1', 'urllc-trf1'  ]
    #         ''', language='python') 
    
    # plt.clf()
    # feature_x2 = st.selectbox('Select KPI for KDE plot', ['tx_brate_norm', 'tx_pkts_norm', 'dl_buffer_norm'])
    # feature_y2 = st.selectbox('Select Split-by cretieron for KDE plot: ', ['tx_brate_norm', 'tx_pkts_norm', 'dl_buffer_norm'])

    # kdeplot = sns.kdeplot(data=c1, x=feature_x2, y=feature_y2, hue='agent', col='slice')
    # st.pyplot(kdeplot.figure.figure)

    # st.divider()  
