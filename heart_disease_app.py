import streamlit as st
import pandas as pd
import numpy as np 


def app():
    st.header(":red[Heart Disease] :green[Prediction]", divider='green')
    
    st.markdown("This project aim to diagnosis and predict the risk of a patient having heart attack and disease at early stage. \
    The goal is to focus on identifying individuals who have the disease so that medical practitioners can administer treatments to them.")
    
    data = pd.read_csv('new_heart_data.csv')
    data = data.drop(["Unnamed: 0", "target"], axis=1)
    
    # Display any 10 random examples(samples) from the whole dataset when a user click on the checkbox. 
    if st.checkbox(label="Click to view dataset"):
        st.write(data.sample(10))
    
    st.write("Wanna make prediction?")
    if st.button('If yes, click on button'):
        """Prompt a user for inputs."""
        
        # Accept the user age.
        age = st.number_input(label="What's your age?", min_value=1, max_value=120, step=1)
        
        # Convert the user sex input into categorical.
        sex = st.radio(label="Are you a female or male?", options=["Female", "Male"])   
        if (sex == "Female"):
            sex = 0
        elif (sex == "Male"):
            sex = 1
        
        # Convert the user's chest pain input into categorical.
        chest_pain = st.radio(label="What's your chest pain type?", options=['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        if (chest_pain == 'Typical Angina'):
            sex = 0
        elif (chest_pain == 'Atypical Angina'):
            sex = 1
        elif (chest_pain == 'Non-anginal Pain'):
            sex = 2
        elif (chest_pain == 'Asymptomatic'):
            sex = 3
        
        # Collect the user's resting blood pressure.
        rbp = st.number_input(label="What is the value of your resting blood pressure?", min_value=0, max_value=500, step=1)
        
        # Accept the user's cholesterol level.
        cholesterol = st.number_input(label="What's your Cholesterol level?", min_value=1, max_value=600)
        
        # Collect the user's fasting blood sugar and convert it into categorical using threshold.
        fbs = st.number_input("What's fasting blood sugar?", min_value=1, max_value=500)
        if (fbs <= 120):
            fbs = 0
        else:
            fbs = 1
            
        # Accept and convert user's resting electro
        rest_ecg = st.radio(label="", options = ['Normal', 'Abnormality', 'Hypertrophy'])
        if (rest_ecg == 'Normal'):
            sex = 0
        elif (rest_ecg == 'Abnormality'):
            sex = 1
        elif (rest_ecg == 'Hypertrophy'):
            sex = 2
        
        # Collect and convert user's exercise induced angina into categorical.
        exer_ind_angina = st.radio(label="", options=["No", "Yes"])
        if (exer_ind_angina == 'No'):
            exer_ind_angina = 0
        elif (exer_ind_angina == 'Yes'):
            exer_ind_angina = 1
   
        
        oldpeak = st.number_input("What's your old peak?")
        
        st_slope = st.radio(label="", options=['Upsloping', 'Flat', 'Downsloping'])
        if (st_slope == 'psloping'):
            st_slope = 0
        elif (st_slope == 'Flat'):
            st_slope = 1
        elif (rest_ecg == 'Downsloping'):
            st_slope = 2
            
            
        colored_by_flor = st.radio(label="What's your coloured by flouroscopy?", options=['0', '1', '2', '3'])
            
            
        thallium = st.radio(label="What's your thallium stress test?", options=['Normal', 'Fixed Defect', 'Reversible Defect'])
        if (thallium == 'Normal'):
            thallium = 0
        elif (thallium == 'Fixed Defect'):
            thallium = 1
        elif (thallium == 'Reversible Defect'):
            thallium = 2
    
    




app()

print('hi')