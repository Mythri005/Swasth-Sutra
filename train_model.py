import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# ✅ Sample dataset for training
data = {
    "age": np.random.randint(20, 70, 200),
    "gender": np.random.randint(0, 2, 200),
    "weight": np.random.randint(50, 100, 200),
    "low_bp": np.random.randint(0, 2, 200),
    "high_bp": np.random.randint(0, 2, 200),
    "sugar": np.random.randint(70, 200, 200),
    "diabetes": np.random.randint(0, 2, 200),
    "heart_disease": np.random.randint(0, 2, 200),
    "menstrual_health": np.random.randint(0, 2, 200)
}

df = pd.DataFrame(data)

df["condition"] = np.select(
    [
        (df["diabetes"] == 1),
        (df["heart_disease"] == 1),
        (df["high_bp"] == 1),
        (df["low_bp"] == 1),
        (df["menstrual_health"] == 1),
    ],
    ["Diabetes", "Heart Disease", "High BP", "Low BP", "Menstrual Health"],
    default="General"
)

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=["condition"]), df["condition"], test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open("ml_model/model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as model.pkl")
