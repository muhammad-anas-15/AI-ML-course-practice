import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================================
# 1. GENERATE SYNTHETIC CUSTOMER DATA
# ==========================================
np.random.seed(42)
n = 300

# Cluster 1: "The Daily Regulars" — visit often, spend moderately
c1_spending = np.random.normal(800, 200, n // 3)
c1_visits = np.random.normal(22, 5, n // 3)
c1_avg = np.random.normal(4.5, 1, n // 3)

# Cluster 2: "The Weekend Treaters" — visit rarely, spend big per visit
c2_spending = np.random.normal(600, 150, n // 3)
c2_visits = np.random.normal(5, 2, n // 3)
c2_avg = np.random.normal(14, 3, n // 3)

# Cluster 3: "The Budget Sippers" — low everything
c3_spending = np.random.normal(120, 40, n - 2 * (n // 3))
c3_visits = np.random.normal(8, 3, n - 2 * (n // 3))
c3_avg = np.random.normal(3.5, 0.8, n - 2 * (n // 3))

df = pd.DataFrame({
    'annual_spending': np.concatenate([c1_spending, c2_spending, c3_spending]),
    'visits_per_month': np.concatenate([c1_visits, c2_visits, c3_visits]),
    'avg_transaction': np.concatenate([c1_avg, c2_avg, c3_avg])
})

print(f"Dataset shape: {df.shape}")
print(df.describe().round(2))

# ==========================================
# 2. FEATURE SCALING (Mandatory!)
# ==========================================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# ==========================================
# 3. FIND OPTIMAL K — Elbow Method
# ==========================================
inertias = []
sil_scores = []
K_range = range(2, 11)

for k in K_range:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_scaled, km.labels_))

# Plot Elbow Curve
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(K_range, inertias, 'o-', color='#14b8a6', linewidth=2)
axes[0].set_xlabel('Number of Clusters (K)')
axes[0].set_ylabel('Inertia (WCSS)')
axes[0].set_title('Elbow Method')
axes[0].grid(alpha=0.2)

axes[1].plot(K_range, sil_scores, 'o-', color='#8b5cf6', linewidth=2)
axes[1].set_xlabel('Number of Clusters (K)')
axes[1].set_ylabel('Silhouette Score')
axes[1].set_title('Silhouette Analysis')
axes[1].grid(alpha=0.2)
plt.tight_layout()
plt.savefig('elbow_silhouette.png', dpi=150)
plt.show()

# ==========================================
# 4. FIT FINAL MODEL (K=3 from the elbow)
# ==========================================
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

print(f"\nFinal Inertia: {kmeans.inertia_:.2f}")
print(f"Silhouette Score: {silhouette_score(X_scaled, kmeans.labels_):.4f}")

# ==========================================
# 5. ANALYZE THE CLUSTERS
# ==========================================
# Add cluster labels and compute cluster statistics
cluster_stats = df.groupby('cluster').agg({
    'annual_spending': ['mean', 'std'],
    'visits_per_month': ['mean', 'std'],
    'avg_transaction': ['mean', 'std']
}).round(2)

print("\n📊 Cluster Profiles:")
print(cluster_stats)

# Give clusters human-readable names
names = {
    0: "The Daily Regulars",
    1: "The Weekend Treaters",
    2: "The Budget Sippers"
}
df['segment'] = df['cluster'].map(names)
print("\nCustomer Segments:")
print(df['segment'].value_counts())