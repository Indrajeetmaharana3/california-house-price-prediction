
import sys
import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Allow Python to find the src package
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Configure the Streamlit page
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Locate the trained model
MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "best_house_price_model.pkl"
)

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# App title and description
st.title("🏠 House Price Prediction")
st.write(
    "Predict the median house value in California "
    "using a Machine Learning model."
)

st.info("Our prediction model uses Random Forest Regression.")

# Collect house details
st.subheader("Enter House Details")

# Input fields for the eight original features
med_inc = st.number_input("Median Income (MedInc)", min_value=0.0, value=3.5)
house_age = st.number_input("House Age (HouseAge)", min_value=0.0, value=30.0)
ave_rooms = st.number_input("Average Rooms (AveRooms)", min_value=0.1, value=5.0)
ave_bedrms = st.number_input("Average Bedrooms (AveBedrms)", min_value=0.0, value=1.0)
population = st.number_input("Population (Population)", min_value=0.0, value=1000.0)
ave_occup = st.number_input("Average Occupancy (AveOccup)", min_value=0.1, value=3.0)
latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, value=34.0)
longitude = st.number_input("Longitude", min_value=-125.0, max_value=-114.0, value=-119.0)

# Predict the house price
if st.button("Predict House Price"):
    input_data = pd.DataFrame([{
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }])

    predicted_value = model.predict(input_data)[0]

    # Dataset target is measured in units of $100,000
    predicted_price = predicted_value * 100_000

    st.success("Prediction completed!")
    st.metric(
        "Predicted Median House Value",
        f"${predicted_price:,.2f}"
    )
