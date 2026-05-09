import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("my_dataset.csv")

X = df[["bpm", "energy", "danceability"]]
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# K = √N (nearest odd)
k = int(np.sqrt(len(X_train)))
if k % 2 == 0:
    k += 1

# Train model
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train_scaled, y_train)

# Evaluate
pred = model.predict(X_test_scaled)

print("K =", k)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

# Predict new data
new = [[128, 90, 85],
       [75, 30, 20],
       [160, 80, 55]]

new_scaled = scaler.transform(new)
print("New Predictions:", model.predict(new_scaled))