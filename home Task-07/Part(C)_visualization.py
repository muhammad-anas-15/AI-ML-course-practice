import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap

# Load data
df = pd.read_csv("my_dataset.csv")

X = df[["bpm", "energy", "danceability"]]
y = df["label"]

# Split + scale
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ───── VIZ 1: K vs Accuracy ─────
k_range = range(1, 50, 2)
train_acc = []
test_acc = []

for k in k_range:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)

    train_acc.append(accuracy_score(y_train, model.predict(X_train_scaled)))
    test_acc.append(accuracy_score(y_test, model.predict(X_test_scaled)))

plt.plot(k_range, train_acc, label="Train")
plt.plot(k_range, test_acc, label="Test")
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.title("K vs Accuracy")
plt.legend()
plt.grid()
plt.savefig("k_accuracy_curve.png")
plt.show()

# ───── VIZ 2: Decision Boundary ─────
X2 = X_train_scaled[:, 1:3]  # energy, danceability

# Convert labels to numbers
y_num = (y_train == "Bop").astype(int)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X2, y_num)

h = 0.05
x_min, x_max = X2[:, 0].min() - 1, X2[:, 0].max() + 1
y_min, y_max = X2[:, 1].min() - 1, X2[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, h),
    np.arange(y_min, y_max, h)
)

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

cmap_light = ListedColormap(["#22d3a722", "#7c5cfc22"])
cmap_bold = ListedColormap(["#22d3a7", "#7c5cfc"])

plt.contourf(xx, yy, Z, cmap=cmap_light)
plt.scatter(X2[:, 0], X2[:, 1], c=y_num, cmap=cmap_bold)

plt.xlabel("Energy (scaled)")
plt.ylabel("Danceability (scaled)")
plt.title("Decision Boundary")
plt.savefig("decision_boundary.png")
plt.show()