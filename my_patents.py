import streamlit as st


def run_patents():
    st.subheader('PATENTS & PUBLICATIONS: ') 
    st.write('[Filed patents list](https://patents.justia.com/inventor/rahul-soundrarajan)')
    md = ('''

        - [O-RAN Near Real-Time (Near-RT) RIC for Traffic Steering](https://www.mavenir.com/portfolio/mavscale/ai-analytics/ran-intelligent-controller-ric/) | [[arXiv](https://arxiv.org/abs/2209.14171), [IEEE](https://www.mavenir.com/resources/network-optimization-non-real-time-ric-trial-analysis/), [Whitepaper](https://www.mavenir.com/resources/mavenirs-ran-intelligent-controller-ric-solution/), [blog](https://www.mavenir.com/blog/building-the-worlds-first-o-ran-compliant-ai-powered-closed-loop-near-rt-ric/)] 
        - [O-RAN Non Real-Time (Non-RT) RIC for Network Optimization](https://www.mavenir.com/portfolio/mavscale/ai-analytics/ran-intelligent-controller-ric/) | [[whitepaper](https://www.mavenir.com/resources/network-optimization-non-real-time-ric-trial-analysis/)] 
        - [Patent filed: Mar 29, 2023, Publication: 20230319662](https://patents.justia.com/assignee/mavenir-system-inc): Reinforcement Learning (RL) based optimization of RRM decisions for HO of individual UEs
        - Patent Granted: Mar 25, 2020, US Patent No. 16/365,802: ML based Network profiling using Config params & PM counters 
        - Patent filed: Jan 20, 2020, US Patent No. 16/748,100: Time Series (ARIMA) based models for predicting Network KPIs
        - Patent Granted: Feb 01, 2019, US Patent No. 16/265,029: ML based Node profiling using Performance Counters
        - Patent filed: Jan 18, 2019, US Patent No. 16/251,797: ML (CART) based Cell characterization using Network KPIs 
        - Patent filed: Dec 28, 2018, US Patent No. 16/235,433: System and Method for predicting KPI in a Wireless Network
        - Patent filed: Dec 31, 2013, India No. 3849/DEL/2013: Location / Positioning systems
        - Patent filed: Nov 28, 2012, India No. 3651/DEL/2012: Optimizing Radio Link Setup in UMTS / 3G Ecosystem
        - Whitepaper: “ML based Node Profiling for Wireless Network Optimization” [[link](https://www.hcltech.com/white-papers/engineering/ai-connect-machine-learning-based-node-profiling-wireless-network)] - Published in GSMAThrive, N. America,Oct’20
        - Whitepaper: “AI Connect: A Machine Learning based Time Series forecast for Wireless Network Optimization” [[link](https://www.hcltech.com/white-papers/engineering/ai-connect-machine-learning-based-text-analytics-approaches-wireless-telco)]
        - Whitepaper: “AI Connect: Machine Learning based Text Analytics approaches for Wireless Telco Networks” [[link](https://www.hcltech.com/white-papers/engineering/ai-connect-machine-learning-based-text-analytics-approaches-wireless-telco)]
        - Whitepaper: “Machine Learning based KPI Prediction for Wireless Network Optimization” [[link](https://www.hcltech.com/white-papers/engineering/machine-learning-based-kpi-prediction-wireless-network-optimization)]
        - Whitepaper: “5G 101 Series : Spectrum allocation , challenges and use cases” [[link](https://www.hcltech.com/white-papers/engineering-and-rd-services/5g-101-series-spectrum-allocation-challenges-use-cases)]
        - O-RAN Blog [[here](https://www.gsmathrive.com/northamerica/2020/10/09/yet-another-o-ran-blog-the-perspective-hcl/)] Published in GSMAThrive - North America, Oct-2020

          ''')
    st.write(md)