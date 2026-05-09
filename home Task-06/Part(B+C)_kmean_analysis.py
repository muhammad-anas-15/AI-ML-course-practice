import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load data
df = pd.read_csv('my_dataset.csv')
X = df.values

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Try K = 2 to 10
inertia = []
silhouette = []
K = range(2, 11)

for k in K:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X_scaled)
    inertia.append(km.inertia_)
    silhouette.append(silhouette_score(X_scaled, labels))

# Plot Elbow + Silhouette
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(K, inertia, 'o-')
plt.title("Elbow Curve")
plt.xlabel("K")
plt.ylabel("Inertia")

plt.subplot(1,2,2)
plt.plot(K, silhouette, 'o-')
plt.title("Silhouette Score")
plt.xlabel("K")

plt.tight_layout()
plt.savefig("elbow_silhouette.png")
plt.show()

# Final model (K=3)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Scatter plot
plt.scatter(df['workout_hours_week'],
            df['protein_intake_g'],
            c=df['cluster'], alpha=0.6)

plt.xlabel("Workout Hours")
plt.ylabel("Protein Intake")
plt.title("Cluster Scatter (K=3)")
plt.savefig("cluster_scatter.png")
plt.show()

# Results
print("Cluster sizes:\n", df['cluster'].value_counts())

centroids = scaler.inverse_transform(kmeans.cluster_centers_)
print("\nCentroids:\n", centroids)

# Predict new points
new = [[11,190,110], [3,55,20], [7,85,40]]
pred = kmeans.predict(scaler.transform(new))

print("\nNew Predictions:", pred)