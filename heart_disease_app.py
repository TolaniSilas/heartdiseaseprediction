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

def main():
    st.write("Wanna make prediction?")
    
    if st.button('If yes, click on button'):
        """Prompt a user for inputs."""
        collect_user_inputs()
        

def perform_prediction():
    # Your prediction logic goes here
    st.write("Prediction will be displayed here.")
    
    

def collect_user_inputs():
    # Accept the user age.
    age = st.number_input(label="What's your age?", min_value=1, max_value=120, step=1)
    
    # Convert the user sex input into categorical.
    gender_options = ["Female", "Male"]
    selected_gender = st.radio(label="Are you female or male?", options=gender_options)
    gender_code = gender_options.index(selected_gender)
    
    # Convert the user's chest pain input into categorical.
    chest_pain_options = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic']
    chest_pain = st.radio(label="What's your chest pain type?", options=chest_pain_options)
    chest_pain_code = chest_pain_options.index(chest_pain)
    
    # Collect the user's resting blood pressure.
    rbp = st.number_input(label="What is the value of your resting blood pressure?", min_value=0, max_value=500, step=1)
    
    # Accept the user's cholesterol level.
    cholesterol = st.number_input(label="What's your Cholesterol level?", min_value=1, max_value=600)
    
    # Collect the user's fasting blood sugar and convert it into categorical using threshold.
    fbs_threshold = 120
    fbs = st.number_input("What's fasting blood sugar?", min_value=1, max_value=500)
    fbs_code = 1 if fbs > fbs_threshold else 0
    
    # Accept and convert user's resting electro
    rest_ecg_options = ['Normal', 'Abnormality', 'Hypertrophy']
    rest_ecg = st.radio(label="What's your resting electrocardiographic results?", options=rest_ecg_options)
    rest_ecg_code = rest_ecg_options.index(rest_ecg)
    
    # Collect and convert user's exercise induced angina into categorical.
    exer_ind_angina_options = ["No", "Yes"]
    exer_ind_angina = st.radio(label="Do you have exercise induced angina?", options=exer_ind_angina_options)
    exer_ind_angina_code = exer_ind_angina_options.index(exer_ind_angina)
    
    oldpeak = st.number_input("What's your old peak?")
    
    st_slope_options = ['Upsloping', 'Flat', 'Downsloping']
    st_slope = st.radio(label="What's your ST slope type?", options=st_slope_options)
    st_slope_code = st_slope_options.index(st_slope)
    
    colored_by_flor_options = ['0', '1', '2', '3']
    colored_by_flor = st.radio(label="What's your coloured by flouroscopy?", options=colored_by_flor_options)
    colored_by_flor_code = colored_by_flor_options.index(colored_by_flor)
    
    thallium_options = ['Normal', 'Fixed Defect', 'Reversible Defect']
    thallium = st.radio(label="What's your thallium stress test result?", options=thallium_options)
    thallium_code = thallium_options.index(thallium)

    # Once all inputs are collected, display the button to trigger the prediction.
    if st.button("Predict"):
        # Call function to perform prediction based on collected inputs
        perform_prediction()



app()

if __name__ == "__main__":
    main()

