import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import plotly.express as px
import plotly.figure_factory as ff


plt.rcParams['figure.figsize'] = [4, 4]


def run_play_with_data():
    #Run Static Analysis
    st.subheader("")
    combo = pd.read_csv('combo.csv')
    c1 = combo[[ 'count_norm', 'tx_brate_norm', 'tx_pkts_norm', 'dl_buffer_norm', 'slice', 'agent']]
    st.write('Data to be analyzed: df.describe()')
    st.write(c1.describe())
    st.divider()
    st.write('Sample preview of data: df.sample(10) | Note, first column is the index of dataframe')
    st.write(c1.sample(10))
    st.divider()
    
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

    feature_x = st.selectbox('Select feature for x axis', [ 'dl_buffer_norm', 'count_norm', 'tx_brate_norm', 'tx_pkts_norm', 'slice', 'agent'])
    feature_y = st.selectbox('Select feature for y axis', [ 'tx_pkts_norm', 'tx_brate_norm', 'count_norm', 'dl_buffer_norm', 'slice', 'agent'])   
    feature_z = st.selectbox('Select the split-by criterion: [slice, agent]', ['slice', 'agent'])

    fig, ax = plt.subplots(figsize=(4, 4))
    # sns.scatterplot(data=c1, x=feature_x, y=feature_y, ax=ax)
    # st.pyplot(fig)
    scatter = px.scatter(data_frame=c1, x=feature_x, y=feature_y, color=feature_z)
    st.plotly_chart(scatter)
    st.divider()

    # st.subheader("Plot of Distribution of KPIs per agent OR per slice")
    # st.code(''' 
    #         #Description of columns:
    #         'count_norm': count of repeats of a particular state [2 means the state has repeated twice]
    #         '{kpi}_norm': normalized value of the KPIs: 'tx_brate', 'tx_pkts', 'dl_buffer'
    #         'slice'     : slice IDs: [0,1,2]
    #         'agent'     : agents: ['embb-trf1', 'embb-trf2', 'urllc-trf1', 'urllc-trf1'  ]
    #         ''', language='python') 
    

    # feature_x = st.selectbox('Select KPI', ['tx_brate_norm', 'tx_pkts_norm', 'dl_buffer_norm'])
    # feature_y = st.selectbox('Select Split-by cretieron: ', ['slice', 'agent'])

    # distplot = sns.displot(data=c1, x=feature_x, hue=feature_y, kind="kde")
    # st.pyplot(distplot.fig)
    # st.divider()  

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

    st.subheader(" Plot of Distribution of KPIs per agent OR per slice")
    st.code(''' 
            #Description of columns:
            'count_norm': count of repeats of a particular state [2 means the state has repeated twice]
            '{kpi}_norm': normalized value of the KPIs: 'tx_brate', 'tx_pkts', 'dl_buffer'
            'slice'     : slice IDs: [0,1,2]
            'agent'     : agents: ['embb-trf1', 'embb-trf2', 'urllc-trf1', 'urllc-trf1'  ]
            ''', language='python') 
    
    plt.clf()
    feature_x2 = st.selectbox('Select KPI ', ['tx_brate_norm', 'tx_pkts_norm', 'dl_buffer_norm'])
    # feature_y2 = st.selectbox('Select Split-by cretieron for KDE plot: ', ['slice', 'agent'])
    feature_z2 = st.selectbox('Select 2nd order split-by criterion', ['slice', 'agent'])

    kdeplot = px.histogram(data_frame=c1, x=feature_x2, color=feature_z2, histnorm='density')
    st.plotly_chart(kdeplot)
    kdeplot = px.density_heatmap(data_frame=c1, x=feature_x2, y=feature_z2)
    st.plotly_chart(kdeplot)
    
    st.divider()  
