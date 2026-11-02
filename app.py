import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("bangalore_house_price_model.pkl")

# Get available categories from the trained model
encoder = (
    model.named_steps["preprocessor"]
    .named_transformers_["cat"]
)

area_types, availability_options, locations = encoder.categories_

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Application title
st.title("🏠 House Price Prediction")
st.write(
    "Enter the details below to estimate "
    "the price of a house in Bangalore."
)

st.divider()

# Input form
with st.form("house_form"):

    st.subheader("House Details")

    area_type = st.selectbox(
        "Area Type",
        options=list(area_types)
    )

    availability = st.selectbox(
        "Availability",
        options=list(availability_options)
    )

    location = st.selectbox(
        "Location",
        options=list(locations)
    )

    col1, col2 = st.columns(2)

    with col1:
        total_sqft = st.number_input(
            "Total Area (sq. ft.)",
            min_value=1.0,
            value=1200.0,
            step=100.0
        )

        bhk = st.number_input(
            "Bedrooms (BHK)",
            min_value=1,
            max_value=20,
            value=2,
            step=1
        )

    with col2:
        bath = st.number_input(
            "Bathrooms",
            min_value=1.0,
            value=2.0,
            step=1.0
        )

        balcony = st.number_input(
            "Balconies",
            min_value=0.0,
            value=1.0,
            step=1.0
        )

    submitted = st.form_submit_button(
        "Predict House Price",
        type="primary",
        use_container_width=True
    )

# Prediction
if submitted:

    input_data = pd.DataFrame([{
        "area_type": area_type,
        "availability": availability,
        "location": location,
        "total_sqft": total_sqft,
        "bath": bath,
        "balcony": balcony,
        "bhk": bhk
    }])

    try:
        prediction = model.predict(input_data)[0]

        st.success("Prediction completed!")

        st.metric(
            label="Estimated House Price",
            value=f"{prediction:,.2f}"
        )

        st.caption(
            "The result uses the same price units "
            "as the training dataset. It is an estimate, "
            "not a guaranteed market price."
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")
