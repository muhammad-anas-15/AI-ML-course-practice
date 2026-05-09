import numpy as np
import pandas as pd

np.random.seed(42)
n = 300

# Features
bpm = np.random.uniform(60, 200, n)
energy = np.random.uniform(0, 100, n)
dance = np.random.uniform(0, 100, n)

# Label logic + noise
score = (
    0.45 * energy/100 +
    0.35 * dance/100 +
    np.where((bpm >= 110) & (bpm <= 150), 0.2, 0) +
    np.random.normal(0, 0.1, n)
)

label = np.where(score > 0.55, "Bop", "Skip")

# DataFrame
df = pd.DataFrame({
    "bpm": bpm,
    "energy": energy,
    "danceability": dance,
    "label": label
})

# Save
df.to_csv("my_dataset.csv", index=False)

print("Dataset created:")
print(df['label'].value_counts())