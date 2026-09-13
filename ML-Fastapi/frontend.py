import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Iris Flower Species Predictor")
st.markdown("Enter the details below:")

# input fields

sepal_length = st.number_input("sepal_length", min_value = 0.01, max_value = 100.00)

sepal_width = st.number_input("sepal_width", min_value = 0.01, max_value = 100.00)

petal_length = st.number_input("petal_length", min_value = 0.01, max_value = 100.00)

petal_width = st.number_input("petal_width", min_value = 0.01, max_value = 100.00)

# button

if st.button("Predict iris flower species"):

    input_data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

   
    response = requests.post(API_URL, json = input_data)

    result = response.json()

    if response.status_code == 200 and 'predicted_species' in result:

        st.success(f"predicted species--> {result['predicted_species']}")

        
