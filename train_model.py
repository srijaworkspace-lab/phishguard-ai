import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset/PhiUSIIL_Phishing_URL_Dataset 2.csv")

# Remove unnecessary columns
data = data.drop(columns=["FILENAME", "URL", "Domain", "Title", "TLD"])

# Features
X = data.drop("label", axis=1)

# Labels
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

import joblib

joblib.dump(model, "phishing_model.pkl")

print("Model Saved Successfully")