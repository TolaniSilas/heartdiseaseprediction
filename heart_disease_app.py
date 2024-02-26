import streamlit as st
import pandas as pd
import numpy as np 



# Configuration of Streamlit Page.
st.set_page_config(
    page_title="Heart Disease Prediction App",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
    )



def collect_user_inputs():
    """A function that prompt the user for inputs."""
    
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


    
def perform_prediction():
    """"A function that perform the presence or absence of heart disease prediction based on the collected input data from the user."""
    
    # Once all inputs are collected, display the button to trigger the prediction.
    if st.button("Predict"):
        
        st.success("Prediction will be displayed here.")




def web_app():
    """"A function that displays the web app."""
    
    # Define the pages.
    pages = ["Home", "Prediction"]
    
    # Create a sidebar with page selection.
    selected_pages = st.sidebar.selectbox("Select Page", pages)
    
    
    # Display content based on selected page.
    if selected_pages == "Home":
        
        # The Home Header.
        st.header(":red[Heart Disease] :green[Prediction] App", divider='green')
        
        st.markdown("This is a web app that predict the presence of heart disease in patients or individuals.")
        
        st.image("patient_care.jpg")
        
        # Read the csv file as a DataFrame.
        data = pd.read_csv('new_heart_data.csv')
        
        # Drop the mentioned columns.
        data = data.drop(["Unnamed: 0", "target"], axis=1)
        
        # Display any 10 random examples(samples) from the whole dataset when a user click on the checkbox. 
        if st.checkbox(label="Click to view dataset"):
            
            st.markdown("Datasets:")
            st.write(data.sample(10))

        
        # HTML code with styling.
        html_code = f"""
        <div style="padding: 10px; background-color: #FF0043; margin-bottom: 0px;">
        <h3 style="color: white;">About the App</h3>
        <p style="color: white;">"This web application aims to diagnose and predict the risk of a patient having a heart attack or heart disease at an early stage. 
        The goal is to focus on identifying individuals who may have the disease so that medical practitioners can administer appropriate treatments to them promptly. 
        By providing timely and accurate assessments, this tool seeks to improve patient outcomes and enhance proactive healthcare management."</p> 
        </div>
        """
        
        # Display the HTML content using st.markdown
        st.markdown(html_code, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("<div style='text-align: center; border: 2px solid black; padding: 10px; border-radius: 30px;'> Developed by Osunba Silas 🚀</div>", unsafe_allow_html=True)
        
        # Add section for social media links
        st.markdown("<div style='text-align: center; margin-top: 20px;'>Connect with me📩</div>", unsafe_allow_html=True)
 
    
        # Add links to your Twitter, LinkedIn, and GitHub accounts along with an image link
        st.markdown("<div style='text-align: center;'>\
            <a href='https://x.com/thaguymaxx' target='_blank'>\
                <img src='https://tse2.mm.bing.net/th?id=OIP.GvhQyyfMGA49XVPJ_uvG0gHaEK&pid=Api&P=0&h=180' alt='Twitter' style='width: 30px; height: 30px;'>\
                    </a> •  \
            <a href='https://www.linkedin.com/in/osunbasilas/' target='_blank'>\
                <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png' alt='LinkedIn' style='width: 30px; height: 30px;'>\
                    </a> •  \
            <a href='https://github.com/TolaniSilas' target='_blank'>\
                <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' alt='GitHub' style='width: 30px; height: 30px;'>\
                    </a>\
                        </div>", unsafe_allow_html=True)
    
    
    elif selected_pages == "Prediction":
        st.title("Prediction")
        
        # Line seperator.
        st.markdown('<hr style="border: 2px solid #ddd;">', unsafe_allow_html=True)
        
        st.write("To predict the presence of heart disease in a patient, fill the necessary input")
        
        st.write("")
        
        # Prompt the user for inputs.
        collect_user_inputs()
        
        # Perform prediction.
        perform_prediction()
        

    






web_app()


