import streamlit as st


def run_ai_model():
    st.header("This pages lists several observations in Q'nA format:")

    st.divider()

    st.subheader("Question: Analyse the distribution of KPIs per slice, per agent for different number of UEs:")

    st.markdown(''':blue[**Note the number of dimensions to plot:**]
                ''')
    st.code(''' 
                    - Slices      : [0, 1, 2]
                    - Agents      : ['urllc-trf1', 'urllc-trf2', 'embb-trf1', 'embb-trf2']
                    - KPIs        : ['tx_brate', 'tx_pkts', 'dl_buffer']
                    - No. of UEs  : [3, 4, 5 ,6]
            ''', language='python')
    
    st.markdown(''':blue[**Each plot below is per KPI which is split into 16 data points per slice x 3 slices:**]
                ''')
    st.write('DL_Buffer:')
    st.image('dl_buffer_multi.png')
    st.write('Tx Pkts:')
    st.image('tx_pkts_multi.png')
    st.write('Tx Brate:')
    st.image('tx_brate_multi.png')

    st.write("**Observations:**")
    md = ('''
          - Each Agent has a different impacts for different slices. There is also variability amongst the agents for different number of UEs.
          - But as observed in the statistical analysis, an agent's impact on the KPI doesn't change based on the number of UEs.

          ''')
    st.write(md)
    st.divider()

    st.subheader("Question: Check for data sufficiency across [agent, slices], build a calssification model to predict the slice given the KPIs:")
    st.code(''' Given an agent: ['urllc-trf1', 'urllc-trf2', 'embb-trf1', 'embb-trf2']
                    - Model Inputs  : ['tx_brate', 'tx_pkts', 'dl_buffer']
                    - Model Ouptput : Predict : ['slice_0', 'slice_1', 'slice_2]
            ''', language='python')
    
    st.markdown(''':blue[**1. Check for samples per agent for data sufficiency :**] ''')
    st.image('samples_per_slice_per_agent.png')

    st.write('After extensive analysis, the following method was used to normalize KPIs:')
    st.code('''
            Criteria used: 
            ‘count of repeat transitions’, ‘tx_brate’, ‘tx_pkts’, ‘dl_buffer’

            Formula for normalization: 
            df[‘normalized_kpi] = ( 𝟄 + df[‘kpi’] - np.min(df[‘kpi’])) / np.max(df[‘kpi’])
            Where ‘𝟄’ = 0.1 x np.max(df[‘kpi’] is added to avoid ‘0’ values.

            ''', language='python')    
    st.divider()

    st.markdown(''':blue[**2. Check for variance of KPI per agent per slice data sufficiency :**] ''')

    st.write('TX Brate per agent per slice:')
    st.image('tx_brate_per_agent_per_slice.png')

    st.write('TX Pkts per agent per slice:')
    st.image('tx_pkts_per_agent_per_slice.png')

    st.write('DL Buffer per agent per slice:')
    st.image('dl_buffer_per_agent_per_slice.png')

    st.divider()

    st.markdown(''':blue[**3. Understand the most impacting KPIs per slice:**] ''')
    st.write('URLLC-TRF1:')
    st.image('urllc-impacting-kpis-per-slice.png')
    st.divider()

    st.markdown(''':blue[**4. Summary for URLLC-TRF1: that has most samples so more suitable for modeling**] ''')
    st.write('URLLC-TRF1:')
    st.image('urllc-trf1-summary.png')
    st.divider()

    st.markdown(''':blue[**5. Pairplot to visualize if there is a separation between slices for URLLC_TRF1 for 3 KPIs:**] ''')
    st.write('URLLC-TRF1: Pairplot to visualize if separation amongst slices is possible:')
    st.image('pariplot_urllctrf1.png')
    st.divider()


    st.markdown(''':blue[**6. Utilize AutoML for modeling.**] ''')
    st.markdown(''':blue[Used TPOT for model selection:https://github.com/EpistasisLab/tpot2/tree/main/Tutorial ] ''')
    st.code(''' 
            #Hyperparameter exploration:
            'xgboost.XGBClassifier': {
                'n_estimators': [100],
                'max_depth': range(1, 11),
                'learning_rate': [1e-3, 1e-2, 1e-1, 0.5, 1.],
                'subsample': np.arange(0.05, 1.01, 0.05),
                'min_child_weight': range(1, 21),
                'n_jobs': [1],
                'verbosity': [0]
            },

            #Final model parameters:
            XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                colsample_bynode=1, colsample_bytree=1, enable_categorical=False,
                gamma=0, gpu_id=-1, importance_type=None,
                interaction_constraints='', learning_rate=1.0, max_delta_step=0,
                max_depth=10, min_child_weight=6, missing=nan,
                monotone_constraints='()', n_estimators=100, n_jobs=1,
                num_parallel_tree=1, objective='multi:softprob', predictor='auto',
                random_state=0, reg_alpha=0, reg_lambda=1, scale_pos_weight=None,
                subsample=0.8, tree_method='exact', validate_parameters=1,
                verbosity=0)
            
            #Overfitting, but its ok as it is an indicative study of effectiveness of Agent.
            Model score: 98.5%

            ''', language='python')

    st.write('URLLC-TRF1: Confusion Matrix showing the predictability of a slice, given KPIs for an agent:')
    st.write('Overfitting, but its ok as it is an indicative study of effectiveness of agent.')
    st.image('confusion_matrix.png')
    st.divider()

    st.markdown(''':blue[**7. Visualize the DTree:**] ''')
    st.image('dtree.png')
    st.divider()

    st.markdown(''':blue[**8. Peaking into the model behavior:**] ''')
    st.image('dtreeviz.png')
    st.divider()

    st.markdown(''':blue[**8. Peaking into the model behavior: 3d**] ''')
    st.image('dtreeviz3d.png')
    st.divider()

    st.markdown(''':blue[**9. Diagnosis of prediction**] ''')
    st.image('dtreeviz_pred.png')
    st.divider()


