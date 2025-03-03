import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load processed data
df = pd.read_csv("processed_data.csv")

# Split into features (X) and target (y)
X = df.drop(columns=['CustomerID', 'Churn'])
y = df['Churn']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Print the feature names used during training
print("Features used for training:", X.columns.tolist())

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

import joblib

# Save the trained model
joblib.dump(model, "churn_model.pkl")

print("✅ Model saved as churn_model.pkl")

