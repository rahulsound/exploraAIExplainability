import streamlit as st


def run_statistical_analysis():
    #run_statistical_analysis
    # st.header("This pages lists several observations in Q'nA format:")

    st.divider()

    st.subheader("Question: Compare the distribution of KPIs for one agent - say URLLC-TRF1 for varying number of UEs:")


    st.markdown(''':blue[**1. Urllc-trf1 transition behavior: Compare experiments with 3UEs v/s 6UEs**] ''')
    st.image('levenes_test.png')
    st.write("**Observations:**")
    md = ('''
          - Reference : https://datatab.net/tutorial/levene-test
          - *If the p-value for the Levene test is greater than .05, then the variances are not significantly different from each other (i.e., the homogeneity assumption of the variance is met). If the p-value for the Levene's test is less than .05, then there is a significant difference between the variances.*

          ''')
    st.write(md)
    md = ('''
            - Since the p-value is greater than 0.05 for all 3 KPIs, the impact on KPI does not change with the number of UEs in the system.
        ''')
    st.write(md)
    st.divider()

    st.markdown(''':blue[**2. Plot the distributions of KPIs per slce per UE - this is again to see if there is a difference in variance based on number of UEs in the system**] ''')
    st.image('violin_per_slice_ues.png')
    st.write("**Observations:**")
    md = ('''
            - There is no significant change in variance for KPIs based on number of UEs in the system.
        ''')
    st.write(md)
    st.divider()

    st.markdown(''':blue[**3. Use scatter plots to visualize distribution of delta KPIs for different number of UEs in the system: :**] ''')
    st.image('scatter_plot_kpis_3_6_ues.png')
    st.write("**Observations:**")
    md = ('''
            - The KDE plot also confirms that KPI variance doesn't change significantly with number of UEs in the system.
        ''')
    st.write(md)
    st.divider()

    st.markdown(''':blue[**3. Use CDF plots to compare KPIs for different UEs - consider URLLF-TRF1 for slice-0 as an example:**] ''')
    st.image('cdfs_for_slice0.png')
    st.write("**Observations:**")
    md = ('''
            - The CDF plot also confirms that KPI variance doesn't change significantly with number of UEs in the system.
        ''')
    st.write(md)
    st.divider()

    st.markdown(''':blue[**4. Use Pairplots to compare KPIs for different UEs - consider URLLF-TRF1 for slice-0 as an example:**] ''')
    st.image('paripolts_for_3_6UEs.png')
    st.write("**Observations:**")
    md = ('''
            - The Pairplot also confirms that KPI variance doesn't change significantly with number of UEs in the system.
        ''')
    st.write(md)
    st.divider()
    
