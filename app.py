import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("flight_price_model.pkl")

# Title
st.title("✈ Flight Price Prediction App")
st.write("Enter flight details to predict ticket price")

# Sidebar
st.sidebar.header("Flight Information")

# Airline
airline = st.sidebar.selectbox(
    "Select Airline",
    ["AirAsia", "Air_India", "GO_FIRST", "Indigo", "SpiceJet", "Vistara"]
)

# Source City
source_city = st.sidebar.selectbox(
    "Source City",
    ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"]
)

# Departure Time
departure_time = st.sidebar.selectbox(
    "Departure Time",
    ["Early_Morning", "Morning", "Afternoon", "Evening", "Night", "Late_Night"]
)

# Stops
stops = st.sidebar.selectbox(
    "Stops",
    ["zero", "one", "two_or_more"]
)

# Arrival Time
arrival_time = st.sidebar.selectbox(
    "Arrival Time",
    ["Early_Morning", "Morning", "Afternoon", "Evening", "Night", "Late_Night"]
)

# Destination City
destination_city = st.sidebar.selectbox(
    "Destination City",
    ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad", "Chennai"]
)

# Class
flight_class = st.sidebar.selectbox(
    "Class",
    ["Economy", "Business"]
)

# Duration
duration = st.sidebar.number_input(
    "Duration (Hours)",
    min_value=1.0,
    max_value=50.0,
    value=2.0
)

# Days Left
days_left = st.sidebar.number_input(
    "Days Left Before Journey",
    min_value=1,
    max_value=50,
    value=10
)

# Encoding Dictionaries
airline_map = {
    "AirAsia": 0,
    "Air_India": 1,
    "GO_FIRST": 2,
    "Indigo": 3,
    "SpiceJet": 4,
    "Vistara": 5
}

source_city_map = {
    "Bangalore": 0,
    "Chennai": 1,
    "Delhi": 2,
    "Hyderabad": 3,
    "Kolkata": 4,
    "Mumbai": 5
}

departure_time_map = {
    "Afternoon": 0,
    "Early_Morning": 1,
    "Evening": 2,
    "Late_Night": 3,
    "Morning": 4,
    "Night": 5
}

stops_map = {
    "one": 0,
    "two_or_more": 1,
    "zero": 2
}

arrival_time_map = {
    "Afternoon": 0,
    "Early_Morning": 1,
    "Evening": 2,
    "Late_Night": 3,
    "Morning": 4,
    "Night": 5
}

class_map = {
    "Business": 0,
    "Economy": 1
}

# Convert Input into Numerical Values
input_data = pd.DataFrame({
    "airline": [airline_map[airline]],
    "source_city": [source_city_map[source_city]],
    "departure_time": [departure_time_map[departure_time]],
    "stops": [stops_map[stops]],
    "arrival_time": [arrival_time_map[arrival_time]],
    "destination_city": [source_city_map[destination_city]],
    "class": [class_map[flight_class]],
    "duration": [duration],
    "days_left": [days_left]
})

# Show Input Data
st.subheader("Input Data")
st.write(input_data)

# Prediction Button
if st.button("Predict Flight Price"):

    prediction = model.predict(input_data)

    st.success(f"Estimated Flight Price: ₹ {prediction[0]:,.2f}")