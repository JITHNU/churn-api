import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jithnuka878",  
    database="CustomerChurn"
)

query = "SELECT * FROM customers"
df = pd.read_sql(query, conn)

conn.close()

print(df.head())

df.dropna(inplace=True)

df = pd.get_dummies(df, columns=['Gender', 'Partner', 'Dependents', 'PhoneService',
                                 'MultipleLines', 'InternetService', 'OnlineSecurity',
                                 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                 'StreamingTV', 'StreamingMovies', 'Contract',
                                 'PaperlessBilling', 'PaymentMethod'], drop_first=True)

# Convert 'Churn' column to binary values (Yes = 1, No = 0)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

df.to_csv("processed_data.csv", index=False)

print("✅ Data preprocessing complete. Saved as processed_data.csv")
