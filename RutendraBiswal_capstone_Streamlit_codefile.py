import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the Linear Regression model
with open(r"C:\Users\ASUS\Downloads\LinearRegressionModel.pkl", 'rb') as lr_file:
    model = pickle.load(lr_file)

# Load the dataset
car = pd.read_csv(r"C:\Users\ASUS\Downloads\Cleaned_Car_data.csv")

# App title
st.title("🚗 Car Price Predictor")

# Sidebar for user inputs
st.sidebar.header("Input Car Details")

# Dropdown for car company
companies = sorted(car['company'].unique())
selected_company = st.sidebar.selectbox("Select the Car Company", ["Select Company"] + companies)

# Dropdown for car model
car_models = sorted(car['name'].unique())
selected_model = st.sidebar.selectbox("Select the Car Model", car_models)

# Dropdown for year
years = sorted(car['year'].unique(), reverse=True)
selected_year = st.sidebar.selectbox("Select the Year of Purchase", years)

# Dropdown for fuel type
fuel_types = car['fuel_type'].unique()
selected_fuel_type = st.sidebar.selectbox("Select the Fuel Type", fuel_types)

# Input for kilometers driven
kilo_driven = st.sidebar.number_input("Enter Kilometers Driven", min_value=0, step=1)

# Predict button
if st.sidebar.button("Predict Price"):
    # Check for valid inputs
    if selected_company == "Select Company":
        st.warning("🚨 Please select a car company.")
    elif not selected_model or not selected_year or not selected_fuel_type:
        st.warning("🚨 Please fill all the fields.")
    else:
        # Prepare the data for prediction
        input_data = pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                  data=np.array([selected_model, selected_company, selected_year, kilo_driven, selected_fuel_type]).reshape(1, 5))
        
        # Make prediction
        prediction = model.predict(input_data)
        predicted_price = np.round(prediction[0], 2)

        # Display inputs and prediction result
        st.subheader("Prediction Result")
        st.write(f"**Selected Car Company:** {selected_company}")
        st.write(f"**Selected Car Model:** {selected_model}")
        st.write(f"**Year of Purchase:** {selected_year}")
        st.write(f"**Fuel Type:** {selected_fuel_type}")
        st.write(f"**Kilometers Driven:** {kilo_driven:,} km")

        st.success(f"💰 The predicted price of the car is **₹{predicted_price:,}**.")

#Footer
st.markdown("""
    ---
    <div style="text-align: center; font-size: 1.25rem; color: #555;">
        Best Predicted Price App © 2025
    </div>
    """, unsafe_allow_html=True)
