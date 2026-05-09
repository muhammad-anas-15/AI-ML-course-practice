import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# PART A — Generate Dataset (300 records)

np.random.seed(42)
n = 300

bpm          = np.random.uniform(60, 200, n)    # Beats per minute  (wide range)
energy       = np.random.uniform(0, 100, n)     # Energy score      (0–100)
danceability = np.random.uniform(0, 100, n)     # Danceability %    (0–100)

# Label logic: high energy + high danceability → Bop
# BPM between 110–150 is sweet spot → bonus score
bpm_bonus = np.where((bpm >= 110) & (bpm <= 150), 0.2, 0.0)

score = (
    0.45 * energy / 100
    + 0.35 * danceability / 100
    + bpm_bonus
    + np.random.normal(0, 0.1, n)   # realistic noise
)

label = np.where(score > 0.55, "Bop", "Skip")

df = pd.DataFrame({
    "bpm":          np.round(bpm, 1),
    "energy":       np.round(energy, 1),
    "danceability": np.round(danceability, 1),
    "label":        label
})

df.to_csv("my_dataset.csv", index=False)

print("=" * 50)
print("PART A — Dataset Generated")
print("=" * 50)
print(f"Shape : {df.shape}")
print(f"Classes:\n{df['label'].value_counts()}\n")

# PART B — Train & Evaluate

df = pd.read_csv("my_dataset.csv")
features = ["bpm", "energy", "danceability"]

X = df[features]
y = df["label"]

# 80/20 split with random_state=42
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale — fit on train only to avoid data leakage
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# K = √N rounded to nearest odd
k_auto = int(np.round(np.sqrt(len(X_train))))
if k_auto % 2 == 0:
    k_auto += 1   # make it odd

knn = KNeighborsClassifier(n_neighbors=k_auto, metric="euclidean")
knn.fit(X_train_scaled, y_train)
preds = knn.predict(X_test_scaled)

print("=" * 50)
print(f"PART B — KNN with K = {k_auto}  (√{len(X_train)} ≈ {k_auto})")
print("=" * 50)
print(f"Accuracy : {accuracy_score(y_test, preds) * 100:.1f}%\n")
print("Classification Report:")
print(classification_report(y_test, preds))

# Predict 3 hand-crafted new songs
new_songs = pd.DataFrame({
    "bpm":          [128,  75, 160],
    "energy":       [ 90,  30,  80],
    "danceability": [ 85,  20,  55],
})
new_songs_scaled = scaler.transform(new_songs)
new_preds = knn.predict(new_songs_scaled)

print("3 New Song Predictions:")
for i, (_, row) in enumerate(new_songs.iterrows()):
    print(f"  Song {i+1}: BPM={row.bpm}, Energy={row.energy}, Dance={row.danceability}"
          f"  →  {new_preds[i]}")

# PART C — Visualizations

# --- VIZ 1: K vs Accuracy Curve ---
k_range   = range(1, 50, 2)
train_acc = []
test_acc  = []
best_k, best_acc = k_auto, 0

for k in k_range:
    m = KNeighborsClassifier(n_neighbors=k)
    m.fit(X_train_scaled, y_train)
    ta = accuracy_score(y_train, m.predict(X_train_scaled))
    va = accuracy_score(y_test,  m.predict(X_test_scaled))
    train_acc.append(ta)
    test_acc.append(va)
    if va > best_acc:
        best_acc = va
        best_k   = k

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(list(k_range), train_acc, "o-", label="Train Accuracy", color="#7c5cfc")
ax.plot(list(k_range), test_acc,  "s-", label="Test Accuracy",  color="#22d3a7")
ax.axvline(best_k, linestyle="--", color="#f5a623", linewidth=1.5,
           label=f"Best K = {best_k}  ({best_acc*100:.1f}%)")
ax.set_xlabel("K Value", fontsize=12)
ax.set_ylabel("Accuracy", fontsize=12)
ax.set_title("K vs Accuracy — Bias-Variance Tradeoff", fontsize=14)
ax.legend()
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig("viz1_k_accuracy.png", dpi=150)
plt.show()
print("\n✅  viz1_k_accuracy.png saved")

# --- VIZ 2: Decision Boundary (using energy & danceability) ---
# Re-train on 2 features only for the 2D plot
X2_train = X_train_scaled[:, 1:3]   # energy, danceability (already scaled)
X2_test  = X_test_scaled[:, 1:3]

# Encode labels numerically for contourf
classes = sorted(y_train.unique())          # ['Bop', 'Skip']
y_train_num = (y_train == classes[0]).astype(int).values  # Bop=1, Skip=0
y_test_num  = (y_test  == classes[0]).astype(int).values

knn_2d = KNeighborsClassifier(n_neighbors=best_k)
knn_2d.fit(X2_train, y_train_num)

h = 0.05
x_min, x_max = X2_train[:, 0].min() - 1, X2_train[:, 0].max() + 1
y_min, y_max = X2_train[:, 1].min() - 1, X2_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = knn_2d.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

cmap_bg   = ListedColormap(["#22d3a722", "#7c5cfc22"])
cmap_dots = ListedColormap(["#22d3a7",   "#7c5cfc"])

fig, ax = plt.subplots(figsize=(10, 7))
ax.contourf(xx, yy, Z, cmap=cmap_bg, alpha=0.8)
ax.scatter(X2_train[:, 0], X2_train[:, 1],
           c=y_train_num, cmap=cmap_dots,
           edgecolors="white", linewidths=0.4, s=40, alpha=0.85)

# Legend patches
from matplotlib.patches import Patch
legend = [Patch(color="#22d3a7", label="Skip"),
          Patch(color="#7c5cfc",  label="Bop")]
ax.legend(handles=legend, fontsize=11)

ax.set_xlabel("Energy (scaled)", fontsize=12)
ax.set_ylabel("Danceability (scaled)", fontsize=12)
ax.set_title(f"KNN Decision Boundary  (K={best_k})", fontsize=14)
plt.tight_layout()
plt.savefig("viz2_decision_boundary.png", dpi=150)
plt.show()
print("✅  viz2_decision_boundary.png saved")

print("\nDone! All parts complete.")