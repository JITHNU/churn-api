import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "Tenure": 12,
    "MonthlyCharges": 75.0,
    "TotalCharges": 900.0,
    "Gender_Male": 1,
    "InternetService_Fiber optic": 1,
    "Contract_One year": 1,
    "PaymentMethod_Electronic check": 1
}

response = requests.post(url, json=data)
print("Response:", response.json())
