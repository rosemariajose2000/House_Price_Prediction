# Bangalore House Price Prediction

## Project Overview
This machine learning project predicts house prices in Bangalore based on features such as location, total square feet, BHK, bathrooms, and balconies. Different regression models are compared to identify the best-performing model.

## Objectives
- Predict house prices using machine learning.
- Explore and preprocess housing data.
- Compare multiple regression algorithms.
- Evaluate models using MAE, RMSE, and R² score.

## Dataset Features
- Area Type
- Availability
- Location
- Total Square Feet
- BHK
- Bath
- Balcony
- **Target:** House Price

## Machine Learning Models
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

## Model Evaluation

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 46.40 | 133.89 | 36.57% |
| Decision Tree | 38.92 | 114.66 | 53.48% |
| Random Forest | 33.62 | 104.42 | 61.42% |
| Gradient Boosting | 39.54 | 100.74 | 64.10% |

Gradient Boosting achieved the highest R² score and lowest RMSE among the tested models.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Joblib


## Run the Streamlit application:
   streamlit run app.py
 

## Conclusion
This project demonstrates how machine learning regression models can estimate Bangalore house prices. Gradient Boosting performed best based on R² and RMSE, achieving an R² score of approximately 64.10%.

*Note: Predictions are estimates and may differ from actual market prices.*


## Streamlit deployment link-Local URL: http://localhost:8502 Network URL: http://192.168.1.3:8502


