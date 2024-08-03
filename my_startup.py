import streamlit as st
import pandas as pd


def run_startup_overview():
    st.subheader('Founding member, VP, ML & Software Engg. | [BlueFusion Inc](https://bluefusion.tech/) | Sep-2022 to Nov-2023 | 1y, 3m')
    st.divider()
    st.write('Summary:')
    st.write('''
        - Unique selling proposition: First-of-its-kind multi-modal, multi-spectrum sensor head with a data-centric architecture for all-weather sensing. 
        - [Secured NSF grant](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2230398&HistoricalAwards=false) ($295K) and filed 5+ utility patents, solution applicable to multiple verticals: automotive, surveillance, and defence. 
        - Designed & implemented novel sensor fusion PoC for object detection, classification with velocity and distance tagging [Engineering Demo]. 
        - Adapted [GitHub repo](https://github.com/toolboc/Intelligent-Video-Analytics-with-NVIDIA-Jetson-and-Microsoft-Azure) for edge to cloud streaming that utilized Azure services: Azure IoT Edge, IoT Hub, Azure Stream Analytics.
        - This fusion PoC helped secure $150K+ credits through start-up inception programs (Microsoft, Nvidia, AWS)
        - Tech Stack: Radar-Camera Fusion, Python, Computer Vision (YOLO), Azure IoT Edge, Hub, Azure IoT Stream Analytics, Nvidia Jetson series
                
             ''')
    st.divider()

def run_startup_research():
    st.subheader('Radar Datasets:')
    st.write('Reference: [link](https://www.mdpi.com/1424-8220/22/11/4208) "Towards Deep Radar Perception for Autonomous Driving: Datasets, Methods, and Challenges"')
    st.image('radar_perception_fwrk.png', width=400)
    st.divider()
    st.write('CONVENTIONAL RADAR DATASETS FOR AUTONOMOUS DRIVING')
    data = pd.read_csv('conv_data.csv')
    st.dataframe(data)
    st.divider()

    st.write('PRE-CFAR DATASETS FOR DETECTION')
    data = pd.read_csv('pre_cfar.csv')
    st.dataframe(data)
    st.divider()

    st.write('4D RADAR DATASETS FOR DETECTION')
    data = pd.read_csv('4d.csv')
    st.dataframe(data)
    st.divider()

    st.write('Most of the references below are from : https://github.com/ZHOUYI1023/awesome-radar-perception.')
    st.divider()

    st.subheader('Radar Signal Processing Reference Papers:')
    md = (''' 
	-	[[link]]((https://ieeexplore.ieee.org/document/8828025/)) The Rise of Radar for Autonomous Vehicles: Signal Processing Solutions and Future Research Directions
	-	[[link]](https://ieeexplore.ieee.org/document/9369027) Signal Processing: Automotive Radar Signal Processing: Research Directions and Practical Challenges 
	-	[[link]](https://ieeexplore.ieee.org/abstract/document/7870764) Signal Processing: Automotive Radars A review of signal processing techniques
	-	[[link]](https://ieeexplore.ieee.org/abstract/document/7870737) Signal Processing: Advances in Automotive Radar A framework on computationally efficient high-resolution frequency estimation
	-	[[link]](https://ieeexplore.ieee.org/document/9127853) MIMO: MIMO Radar for Advanced Driver-Assistance Systems and Autonomous Driving: Advantages and Challenges
	-	[[link]](https://ieeexplore.ieee.org/abstract/document/9099537) DOA: Calibration and Direction-of-Arrival Estimation of mm-Wave Radars: A Practical Introduction
	-	[[link]](https://ieeexplore.ieee.org/document/8828004) Digital Radar: High-Performance Automotive Radar: A Review of Signal Processing Algorithms and Modulation Schemes
	-	[[link]](https://ieeexplore.ieee.org/document/1603402) Micro-Doppler: Micro-Doppler Effect in Radar: Phenomenon, Model, and Simulation Study
	-	[[link]](https://ieeexplore.ieee.org/document/9114607) Dynamic Range: Dynamic Range Considerations for Modern Digital Array Radars
	-	[[link]](https://ieeexplore.ieee.org/document/8827996) Phase Noise: On the Safe Road Toward Autonomous Driving: Phase Noise Monitoring in Radar Sensors for Functional Safety Compliance
	-	[[link]](https://ieeexplore.ieee.org/document/9875949) Phase Noise: Detailed Analysis and Modeling of Phase Noise and Systematic Phase Distortions in FMCW Radar Systems
	-	[[link]](https://ieeexplore.ieee.org/document/9127843) Interference: Radar Interference Mitigation for Automated Driving: Exploring Proactive Strategies
	-	[[link]](https://ieeexplore.ieee.org/document/8828037) Interference: Interference in Automotive Radar Systems: Characteristics, Mitigation Techniques, and Current and Future Research

''')
    st.write(md)
    st.divider()

    st.subheader('General Object Detection Reference papers:')
    md = ('''
        -   [[link]](https://arxiv.org/abs/2202.02980) 3D Object Detection from Images for Autonomous Driving: A Survey
        -   [[link]](https://arxiv.org/abs/1912.12033) Deep Learning for 3D Point Clouds: A Survey
        -   [[link]](https://arxiv.org/abs/2111.07624) Attention Mechanisms in Computer Vision: A Survey
        -   [[link]](https://arxiv.org/abs/2011.10671) A Review and Comparative Study on Probabilistic Object Detection in Autonomous Driving
          ''')
    st.write(md)
    st.divider()

    st.subheader('Sensor Fusion Reference papers:')
    md = ('''
        -   [[link]](https://arxiv.org/abs/2106.12735) Learning: Multi-Modal 3D Object Detection in Autonomous Driving: a Survey
        -   [[link]](https://ieeexplore.ieee.org/document/9000872) Learning: Deep Multi-Modal Object Detection and Semantic Segmentation for Autonomous Driving: Datasets, Methods, and Challenges
        -   [[link]](https://www.sciencedirect.com/science/article/abs/pii/S1566253511000558) Traditional: Multisensor data fusion: A review of the state-of-the-art
        -   [[link]](https://www.mdpi.com/1099-4300/20/4/307) Information: Information Decomposition of Target Effects from Multi-Source Interactions: Perspectives on Previous, Current and FutureWork
        -   [[link]](https://link.springer.com/article/10.1007/s10994-021-05946-3)Uncertainty: Aleatoric and Epistemic Uncertainty in Machine Learning: An Introduction to Concepts and Methods
        -   [[link]](https://arxiv.org/abs/2011.10671)Conformal Prediction: A Review and Comparative Study on Probabilistic Object Detection in Autonomous Driving
          ''')
    st.write(md)
    st.divider()

    st.subheader('Survey of approaches from related papers:')
    st.write('[[link]](https://ieeexplore.ieee.org/abstract/document/9674901) 2022-A Machine Learning Perspective on Automotive Radar Direction of Arrival Estimation ')
    st.image('doa_estim.png', width=400)
    st.divider()
    st.image('doa2.png', width=400)
    st.divider()

    st.write('[[link]](https://ieeexplore.ieee.org/abstract/document/9561938) 2021-A Continuous-Time Approach for 3D Radar-to-Camera Extrinsic Calibration ICRA; Motion ')
    st.image('rad_cam_rig.png', width=400)
    st.divider()

    st.write('[[link]](https://ieeexplore.ieee.org/document/8917135) 2019-Targetless Rotational Auto-Calibration of Radar and Camera for Intelligent Transportation Systems ITSC; NN ')
    st.image('calib.png', width=400)
    st.divider()

    st.write('[[link]](https://ieeexplore.ieee.org/document/1334537/) 2004-Obstacle Detection Using Millimeter-wave Radar and Its Visualization on Image Sequence ICPR;  ')
    st.image('rad_cam_geo.png', width=400)
    st.image('decision_process_rad.png', width=400)
    st.divider()


    st.subheader('Radar Camera Fusion:')
    st.write('[[link]](https://arxiv.org/pdf/1901.10951) 2019-Distant Vehicle Detection Using Radar and Vision:')
    st.image('veh_detect.png', width=400)
    st.image('sensor_layout.png', width=400)
    st.image('fig3_bbox.png', width=400)
    st.divider()

    st.write('[[link]](https://arxiv.org/pdf/2003.01816.pdf) RODNet: Radar Object Detection using Cross-Modal Supervision ')
    st.image('rodnet.png', width=400)
    st.divider()

    
    st.write('[[link]](https://patrick-llgc.github.io/Learning-Deep-Learning/paper_notes/rvnet.html) RVNet: Deep Sensor Fusion of Monocular Camera and Radar for Image-based Obstacle Detection in Challenging Environments ')
    st.image('rvnet_3.png', width=400)
    st.image('rvnet_4.png', width=400)
    st.image('rvnet_5.png', width=400)
    st.image('rvnet_5.png', width=400)
    st.divider()

    st.write('[[link]]("https://ml4ad.github.io/files/papers/Radar%20and%20Camera%20Early%20Fusion%20for%20Vehicle%20Detection%20in%20Advanced%20Driver%20Assistance%20Systems.pdf") 2019-Radar and Camera Early Fusion for Vehicle Detection in Advanced Driver Assistance Systems  ')
    st.image('qfig1.png', width=400)
    st.image('qfig2.png', width=400)
    st.image('rvnet_5.png', width=400)
    st.image('rvnet_5.png', width=400)
    st.divider()

    st.subheader('Experiments conducted for PoC:')
    data = pd.read_csv('exps_conducted.csv')
    st.dataframe(data)
    st.divider()    

def run_prototyping():
    st.subheader('List of open-source repositories and dev kits used for prototyping [non-NDA]')
    st.divider()

    st.write('Utilize SenseCAP AI sensor series from Seeedstudio:')
    st.image('seeed.png', width=600)
    st.image('seeed2.png', width=600)
    st.divider()

    st.write('[[link]](https://www.kaggle.com/datasets/benceveges/yolo-flir) Custom Object training experiments with FLIR dataset')
    st.write('Custom object detection outputs based on YOLOV5:')
    st.image('yolo-flir.png', width=600)
    st.write('Increased detections with custom-object detection methodology compared to vanila YOLO:')
    st.image('yolo-flir2.png', width=600)
    st.write('Custom Object training - comparison of loss curves on Comet:')
    st.image('comet.png', width=600)


    st.write('[[link]](https://github.com/toolboc/Intelligent-Video-Analytics-with-NVIDIA-Jetson-and-Microsoft-Azure) The project makes use of the NVIDIA DeepStream SDK running on NVIDIA Jetson Embedded hardware to produce an Intelligent Video Analytics Pipeline.')

    st.image('azure_archi.png', width=600)
    st.divider()
    st.write('Simplified view:')
    st.image('hld-archi.png', width=600)
    st.divider()
    st.write('End-to-end view:')
    st.image('toolboc-adaptation.png', width=600)
    st.divider()

    st.write('[[link]](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/video-analytics) Reference Architecture from MS Azure for Video Analytics - to tackle camera-only stream:')
    st.image('azure_idea1.png', width=600)
    st.image('azure_idea2.png', width=600)
    st.divider()

    st.write('[[link]](https://github.com/rahulsound/radcamfusion/blob/main/demo-v1.gif) Sample demo from BlueFusion sensor head with hardware synchronized radar+camera dataset collected at UCSD with a custom object detection model based on YOLOV8:')
    st.image('demo.png', width=800)
    st.divider()


################################################
def run_startup():
    menu = ["Overview",
            "Research", 
            "Rapid Prototyping"
            ]

    choice = st.sidebar.radio("Menu", menu)
    if choice == "Overview":
        run_startup_overview()
    elif choice == "Research":
        run_startup_research()
    elif choice == "Rapid Prototyping":
        run_prototyping()

