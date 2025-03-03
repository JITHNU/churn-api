import joblib
import pandas as pd

# Load trained model
model = joblib.load("churn_model.pkl")

# List of all features from training (copy-paste from `train_model.py` output)
expected_features = ['SeniorCitizen', 'Tenure', 'MonthlyCharges', 'TotalCharges', 'Gender_Male',
                     'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No phone service',
                     'MultipleLines_Yes', 'InternetService_Fiber optic', 'InternetService_No',
                     'OnlineSecurity_No internet service', 'OnlineSecurity_Yes', 'OnlineBackup_No internet service',
                     'OnlineBackup_Yes', 'DeviceProtection_No internet service', 'DeviceProtection_Yes',
                     'TechSupport_No internet service', 'TechSupport_Yes', 'StreamingTV_No internet service',
                     'StreamingTV_Yes', 'StreamingMovies_No internet service', 'StreamingMovies_Yes',
                     'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes',
                     'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check',
                     'PaymentMethod_Mailed check']

# Create a sample customer with all features set to 0
sample_data = pd.DataFrame([{feature: 0 for feature in expected_features}])

# Fill in relevant values for the prediction
sample_data["Tenure"] = 12
sample_data["MonthlyCharges"] = 75.0
sample_data["TotalCharges"] = 900.0
sample_data["Gender_Male"] = 1
sample_data["InternetService_Fiber optic"] = 1
sample_data["Contract_One year"] = 1
sample_data["PaymentMethod_Electronic check"] = 1

# Ensure columns are in the same order as training
sample_data = sample_data[expected_features]

# Make prediction
prediction = model.predict(sample_data)

print("Prediction:", "Churn" if prediction[0] == 1 else "No Churn")
