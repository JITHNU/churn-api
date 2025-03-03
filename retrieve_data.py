import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jithnuka878",  # Replace with your actual MySQL password
    database="CustomerChurn"
)

# SQL query to get all customer data
query = "SELECT * FROM customers"
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display first 5 rows
print(df.head())

# Handle missing values
df.dropna(inplace=True)

# Convert categorical variables to numerical (One-Hot Encoding)
df = pd.get_dummies(df, columns=['Gender', 'Partner', 'Dependents', 'PhoneService',
                                 'MultipleLines', 'InternetService', 'OnlineSecurity',
                                 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                 'StreamingTV', 'StreamingMovies', 'Contract',
                                 'PaperlessBilling', 'PaymentMethod'], drop_first=True)

# Convert 'Churn' column to binary values (Yes = 1, No = 0)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Save processed data
df.to_csv("processed_data.csv", index=False)

print("✅ Data preprocessing complete. Saved as processed_data.csv")
