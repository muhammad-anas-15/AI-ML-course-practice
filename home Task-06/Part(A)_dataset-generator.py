import numpy as np
import pandas as pd

np.random.seed(42)

# Create 3 clusters (100 each)
c1 = np.random.normal([8, 80, 45], [2, 20, 12], (100, 3))
c2 = np.random.normal([12, 200, 120], [3, 40, 30], (100, 3))
c3 = np.random.normal([3, 60, 25], [1.5, 15, 8], (100, 3))

# Combine
data = np.vstack([c1, c2, c3])

df = pd.DataFrame(data, columns=[
    'workout_hours_week',
    'protein_intake_g',
    'monthly_spend_usd'
])

# Add noise
df += np.random.normal(0, [0.5, 10, 5], df.shape)

df.to_csv('my_dataset.csv', index=False)

print("Dataset created:", df.shape)
print(df.head())