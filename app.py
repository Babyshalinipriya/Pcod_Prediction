import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to preprocess user inputs
def preprocess_inputs(age, weight, height, bmi, blood_group, pulse_rate, rr, cycle, cycle_length,
                      marriage_status, pregnant, abortions, hip, waist, weight_gain, hair_growth, 
                      skin_darkening, hair_loss, pimples, fast_food, reg_exercise):
    # Map categorical variables to numerical values
    blood_group_map = {'A': 0, 'B': 1, 'AB': 2, 'O': 3}
    cycle_map = {'Regular': 0, 'Irregular': 1}
    pregnant_map = {'Yes': 0, 'No': 1}
    weight_gain_map = {'Yes': 0, 'No': 1}
    hair_growth_map = {'Yes': 0, 'No': 1}
    skin_darkening_map = {'Yes': 0, 'No': 1}
    hair_loss_map = {'Yes': 0, 'No': 1}
    pimples_map = {'Yes': 0, 'No': 1}
    fast_food_map = {'Yes': 0, 'No': 1}
    reg_exercise_map = {'Yes': 0, 'No': 1}
    
    # Convert categorical variables to numerical
    blood_group = blood_group_map.get(blood_group, 0)  # default 0 if not found
    cycle = cycle_map.get(cycle, 0)  # default 0 if not found
    pregnant = pregnant_map.get(pregnant, 0)
    weight_gain = weight_gain_map.get(weight_gain, 0)
    hair_growth = hair_growth_map.get(hair_growth, 0)
    skin_darkening = skin_darkening_map.get(skin_darkening, 0)
    hair_loss = hair_loss_map.get(hair_loss, 0)
    pimples = pimples_map.get(pimples, 0)
    fast_food = fast_food_map.get(fast_food, 0)
    reg_exercise = reg_exercise_map.get(reg_exercise, 0)
    
    # Return a list of preprocessed inputs
    return [age, weight, height, bmi, blood_group, pulse_rate, rr, cycle, cycle_length,
            marriage_status, pregnant, abortions, hip, waist, weight_gain, hair_growth, 
            skin_darkening, hair_loss, pimples, fast_food, reg_exercise]

# Function to make prediction
def predict_pcos(inputs):
    # Make prediction
    prediction = model.predict([inputs])
    if prediction[0] == 1:
        return "PCOS is present"
    else:
        return "PCOS is not present"

# CSS styling
st.markdown(
    """
    <style>
    /* Add some padding to inputs */
    .stTextInput > div > div > div > input {
        padding: 8px;
    }
    
    /* Style the 'Predict' button */
    .stButton > button {
        color: #ffffff;
        background-color: #008CBA;
        padding: 8px 12px;
        border-radius: 5px;
    }
    
    /* Style the 'Predict' button on hover */
    .stButton > button:hover {
        background-color: #005F6B;
    }

    /* Increase font size and add some padding to the outputs */
    .stText {
        font-size: 18px;
        padding: 10px 0;
    }
    
    /* Hide the sidebar by default */
    .sidebar-content {
        display: none;
    }
    
    /* Style the sidebar icon */
    #sidebar-icon {
        position: fixed;
        top: 20px;
        left: 20px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('', ['Homepage', 'Prediction'])

# Homepage content
if page == 'Homepage':
    st.title('PCOS Predictor')

    st.header('Overview of PCOS and PCOD:')
    st.write('Polycystic ovary syndrome (PCOS) is a hormonal disorder common among women of reproductive age. Women with PCOS may have infrequent or prolonged menstrual periods or excess male hormone (androgen) levels. The ovaries may develop numerous small collections of fluid (follicles) and fail to regularly release eggs.')
    st.write('Polycystic ovary disease (PCOD) is a condition in which multiple small cysts (fluid-filled sacs) develop in the ovaries. The cysts are not harmful but lead to hormone imbalances.')
    st.write('Both PCOS and PCOD can lead to symptoms such as irregular periods, weight gain, acne, and hair growth in unwanted areas.')

    st.header('Self-care steps for PCOD:')
    st.write('1. Maintain a healthy weight through diet and exercise.')
    st.write('2. Eat a balanced diet rich in fruits, vegetables, whole grains, and lean proteins.')
    st.write('3. Exercise regularly to help regulate menstrual cycles and reduce insulin resistance.')
    st.write('4. Manage stress through relaxation techniques such as yoga or meditation.')
    st.write('5. Avoid smoking and limit alcohol consumption.')

# Prediction page content
elif page == 'Prediction':
    st.title('PCOS Predictor')

    # Get user inputs
    age = st.number_input('Age (years)', value=0, step=1)
    weight = st.number_input('Weight (Kg)', value=0, step=1)
    height = st.number_input('Height (cm)', value=0, step=1)
    bmi = st.number_input('BMI', value=0, step=1)
    blood_group = st.selectbox('Blood Group', ['A', 'B', 'AB', 'O'])
    pulse_rate = st.number_input('Pulse rate (bpm)', value=0, step=1)
    rr = st.number_input('RR (breaths/min)', value=0, step=1)
    cycle = st.selectbox('Cycle (R/I)', ['Regular', 'Irregular'])
    cycle_length = st.number_input('Cycle length (days)', value=0, step=1)
    marriage_status = st.number_input('Marriage Status (years)', value=0, step=1)
    pregnant = st.selectbox('Pregnant ', ['Yes', 'No'])
    abortions = st.number_input('No. of abortions', value=0, step=1)
    hip = st.number_input('Hip (inch)', value=0, step=1)
    waist = st.number_input('Waist (inch)', value=0, step=1)
    weight_gain = st.selectbox('Weight gain ', ['Yes', 'No'])
    hair_growth = st.selectbox('Hair growth ', ['Yes', 'No'])
    skin_darkening = st.selectbox('Skin darkening (Y/N)', ['Yes', 'No'])
    hair_loss = st.selectbox('Hair loss ', ['Yes', 'No'])
    pimples = st.selectbox('Pimples ', ['Yes', 'No'])
    fast_food = st.selectbox('Fast food ', ['Yes', 'No'])
    reg_exercise = st.selectbox('Reg.Exercise ', ['Yes', 'No'])

    # When 'Predict' button is clicked, make prediction
    if st.button('Predict'):
        # Preprocess inputs
        inputs = preprocess_inputs(age, weight, height, bmi, blood_group, pulse_rate, rr, cycle, cycle_length,
                                   marriage_status, pregnant, abortions, hip, waist, weight_gain, hair_growth, 
                                   skin_darkening, hair_loss, pimples, fast_food, reg_exercise)
        # Predict PCOS
        prediction = predict_pcos(inputs)
        st.write(prediction)
