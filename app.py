import streamlit as st
import pickle
import numpy as np

# Load the trained model

with open("linear_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("California Housing Price Prediction 🏡")

st.markdown("Enter values below to predict median house value:")


MedInc = st.number_input("Median Income (in 10k$)", min_value=0.0, max_value=20.0, value=3.0, step=0.1)
HouseAge = st.number_input("House Age", min_value=1, max_value=100, value=20)
AveRooms = st.number_input("Average Rooms", min_value=1.0, max_value=50.0, value=5.0, step=0.1)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.5, max_value=10.0, value=1.0, step=0.1)
Population = st.number_input("Population", min_value=1, max_value=40000, value=1000)
AveOccup = st.number_input("Average Occupants per Household", min_value=1.0, max_value=50.0, value=3.0, step=0.1)
Latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, value=36.0, step=0.01)
Longitude = st.number_input("Longitude", min_value=-125.0, max_value=-113.0, value=-120.0, step=0.01)

# Prepare the input
features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])

# Predict and show result
if st.button("Predict"):
    prediction = model.predict(features)[0]
    st.success(f"🏠 Predicted Median House Value: ${prediction * 100000:,.2f}")

