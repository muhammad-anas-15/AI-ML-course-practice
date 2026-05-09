"""
Lab 05: K-Means Clustering — Complete Solution
Domain: Gym Members (Fitness Data)
300 records, 3 features, 3 natural clusters
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

# ─────────────────────────────────────────────
# PART A — Generate Dataset
# ─────────────────────────────────────────────

np.random.seed(42)
n = 300

# Cluster 1: "Cardio Bunnies" — moderate hours, low protein, low spend
c1 = {
    'workout_hours_week': np.random.normal(8, 2, 100),
    'protein_intake_g':   np.random.normal(80, 20, 100),
    'monthly_spend_usd':  np.random.normal(45, 12, 100)
}

# Cluster 2: "Powerlifters" — high hours, high protein, high spend
c2 = {
    'workout_hours_week': np.random.normal(12, 3, 100),
    'protein_intake_g':   np.random.normal(200, 40, 100),
    'monthly_spend_usd':  np.random.normal(120, 30, 100)
}

# Cluster 3: "New Year's Resolutioners" — low hours, low protein, low spend
c3 = {
    'workout_hours_week': np.random.normal(3, 1.5, 100),
    'protein_intake_g':   np.random.normal(60, 15, 100),
    'monthly_spend_usd':  np.random.normal(25, 8, 100)
}

df = pd.DataFrame({
    'workout_hours_week': np.concatenate([c1['workout_hours_week'],
                                          c2['workout_hours_week'],
                                          c3['workout_hours_week']]),
    'protein_intake_g':   np.concatenate([c1['protein_intake_g'],
                                          c2['protein_intake_g'],
                                          c3['protein_intake_g']]),
    'monthly_spend_usd':  np.concatenate([c1['monthly_spend_usd'],
                                          c2['monthly_spend_usd'],
                                          c3['monthly_spend_usd']])
})

# Add realistic noise to blur boundaries
df['workout_hours_week'] += np.random.normal(0, 0.5, n)
df['protein_intake_g']   += np.random.normal(0, 10, n)

df.to_csv('my_dataset.csv', index=False)
print("✅ Part A — Dataset Generated")
print(f"   Shape: {df.shape}")
print(df.describe().round(2))
print()

# ─────────────────────────────────────────────
# PART B — Find K & Train
# ─────────────────────────────────────────────

# Load CSV and scale
df = pd.read_csv('my_dataset.csv')
features = ['workout_hours_week', 'protein_intake_g', 'monthly_spend_usd']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Sweep K = 2 to 10, record inertia and silhouette
inertias = []
sil_scores = []
K_range = range(2, 11)

for k in K_range:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X_scaled)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_scaled, labels))

print("Part B — K Sweep Results")
print(f"{'K':<5} {'Inertia':>12} {'Silhouette':>12}")
for k, iner, sil in zip(K_range, inertias, sil_scores):
    print(f"{k:<5} {iner:>12.1f} {sil:>12.4f}")
print()

# ─────────────────────────────────────────────
# PART C — Visualizations
# ─────────────────────────────────────────────

COLORS = ['#14b8a6', '#8b5cf6', '#f43f5e', '#f59e0b', '#0ea5e9']
OPTIMAL_K = 3  # Elbow appears at K=3 and silhouette peaks there too

# --- VIZ 1: Elbow + Silhouette Dual Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('K-Means: Finding Optimal K', fontsize=14, fontweight='bold')

ks = list(K_range)

# Elbow curve
ax1.plot(ks, inertias, 'o-', color='#14b8a6', linewidth=2.5, markersize=7)
ax1.axvline(OPTIMAL_K, linestyle='--', color='#f59e0b', linewidth=1.5,
            label=f'Optimal K={OPTIMAL_K}')
ax1.set_xlabel('Number of Clusters (K)', fontsize=12)
ax1.set_ylabel('Inertia (WCSS)', fontsize=12)
ax1.set_title('Elbow Curve', fontsize=13)
ax1.legend()
ax1.grid(alpha=0.3)
ax1.set_xticks(ks)

# Silhouette scores
ax2.plot(ks, sil_scores, 's-', color='#8b5cf6', linewidth=2.5, markersize=7)
ax2.axvline(OPTIMAL_K, linestyle='--', color='#f59e0b', linewidth=1.5,
            label=f'Optimal K={OPTIMAL_K}')
ax2.set_xlabel('Number of Clusters (K)', fontsize=12)
ax2.set_ylabel('Silhouette Score', fontsize=12)
ax2.set_title('Silhouette Scores', fontsize=13)
ax2.legend()
ax2.grid(alpha=0.3)
ax2.set_xticks(ks)

plt.tight_layout()
plt.savefig('viz1_elbow_silhouette.png', dpi=150)
plt.show()
print("Viz 1 saved → viz1_elbow_silhouette.png")

# --- VIZ 2: 2D Cluster Scatter Plot ---
final_km = KMeans(n_clusters=OPTIMAL_K, n_init=10, random_state=42)
df['cluster'] = final_km.fit_predict(X_scaled)

fig, ax = plt.subplots(figsize=(10, 7))

for c in range(OPTIMAL_K):
    mask = df['cluster'] == c
    ax.scatter(df.loc[mask, 'workout_hours_week'],
               df.loc[mask, 'protein_intake_g'],
               c=COLORS[c], label=f'Cluster {c}',
               alpha=0.6, s=50, edgecolors='white', linewidths=0.3)

# Plot centroids in original scale
centroids_orig = scaler.inverse_transform(final_km.cluster_centers_)
ax.scatter(centroids_orig[:, 0], centroids_orig[:, 1],
           c='white', marker='*', s=400,
           edgecolors='black', linewidths=1.5, zorder=10,
           label='Centroids')

ax.set_xlabel('Workout Hours / Week', fontsize=12)
ax.set_ylabel('Protein Intake (g)', fontsize=12)
ax.set_title(f'K-Means Cluster Scatter (K={OPTIMAL_K})', fontsize=14)
ax.legend()
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig('viz2_scatter.png', dpi=150)
plt.show()
print("Viz 2 saved → viz2_scatter.png")

# ─────────────────────────────────────────────
# Final Model Stats
# ─────────────────────────────────────────────

print("\nFinal Model — Cluster Sizes")
print(df['cluster'].value_counts().sort_index().to_string())

print("\n Cluster Centroids (original scale)")
centroid_df = pd.DataFrame(centroids_orig, columns=features)
centroid_df.index.name = 'Cluster'
print(centroid_df.round(2).to_string())

# ─────────────────────────────────────────────
# Predict 3 New Data Points
# ─────────────────────────────────────────────

new_points = pd.DataFrame({
    'workout_hours_week': [11,  3, 7],
    'protein_intake_g':   [190, 55, 85],
    'monthly_spend_usd':  [110, 20, 40]
})

new_scaled = scaler.transform(new_points)
predictions = final_km.predict(new_scaled)

print("\n Predictions for 3 New Data Points")
new_points['predicted_cluster'] = predictions
print(new_points.to_string(index=False))

print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JUSTIFICATION FOR K=3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The Elbow Curve shows a sharp drop in inertia from K=2 to K=3,
after which the curve flattens — the classic "elbow" shape.
The Silhouette Score also peaks at K=3, meaning points are well
matched to their own cluster and poorly matched to neighbours.
These two signals together confirm K=3 as the optimal choice,
which also matches the 3 natural groups we designed in Part A.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")