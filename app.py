import streamlit as st
import requests
import datetime
import pandas as pd
import numpy as np

# Title
st.title("Taxi Fare Prediction App 🚖")

# API URL (ensure this is correct)
API_URL = "https://taxifare-842420146816.europe-west1.run.app/predict"

# Collect user input
st.subheader("Enter Ride Details:")
pickup_date = st.date_input("Pickup Date", datetime.date.today())
pickup_time = st.time_input("Pickup Time", datetime.datetime.now().time())
pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)

pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)

# Create API request payload
params = {
    "pickup_datetime": pickup_datetime.strftime("%Y-%m-%d %H:%M:%S"),
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}


# Call API on button click
if st.button("Predict Fare"):
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        print(response.json().get("fare"))
        st.write(response.json().get("fare"))
    else:
        print("ERROR")

# Add a MAP
def get_map_data():

    return pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)
