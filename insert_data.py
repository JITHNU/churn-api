import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="Jithnuka878",  
    database="CustomerChurn"
)
cursor = conn.cursor()

# Load CSV file
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Convert 'TotalCharges' to numeric (handle empty values)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.fillna(0, inplace=True)

# SQL query for inserting data
insert_query = """
INSERT INTO customers 
(CustomerID, Gender, SeniorCitizen, Partner, Dependents, Tenure, PhoneService, MultipleLines, 
InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, 
StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Insert data row by row
for _, row in df.iterrows():
    values = tuple(row)
    cursor.execute(insert_query, values)

# Commit and close connection
conn.commit()
conn.close()

print("✅ Data successfully inserted into MySQL!")
