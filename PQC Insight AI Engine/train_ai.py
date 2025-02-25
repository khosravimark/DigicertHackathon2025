import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load training data
df = pd.read_csv("pqc_training_data.csv")

# Encode categorical columns
encoders = {}
for col in ["OS Type", "Crypto Library", "Web Server", "Cert Type"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le  # Save the encoder per column

# Save the label encoders correctly
with open("label_encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

# Train a model
X = df.drop(columns=["PQC Compatible", "Best PQC Algorithm", "Upgrade Steps"])
y = df["PQC Compatible"]
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model
with open("pqc_model.pkl", "wb") as f:
    pickle.dump(model, f)

