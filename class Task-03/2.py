import numpy as np

np.random.seed(42)   # reproducible results

scores = np.random.randint(40, 101, size=(100, 5))
subjects = ["Math", "Physics", "Programming", "AI", "English"]

print("Scores Matrix (first 5 students):")
print(scores[:5])
print()

# -------- (a) Mean, Median, Std for each subject --------
mean_scores = np.mean(scores, axis=0)
median_scores = np.median(scores, axis=0)
std_scores = np.std(scores, axis=0)

print("Mean Scores:", mean_scores)
print("Median Scores:", median_scores)
print("Std Deviation:", std_scores)
print()

# -------- (b) Pass / Fail count --------
passed = np.sum(scores >= 50, axis=0)
failed = np.sum(scores < 50, axis=0)

print("Students Passed per Subject:", passed)
print("Students Failed per Subject:", failed)
print()

# -------- (c) Overall Topper --------
totals = np.sum(scores, axis=1)
topper_index = np.argmax(totals)
topper_score = totals[topper_index]

print("Topper Student Index:", topper_index)
print("Topper Total Score:", topper_score)
print()

# -------- (d) Grade Distribution --------
A = np.sum(scores >= 90, axis=0)
B = np.sum((scores >= 75) & (scores < 90), axis=0)
C = np.sum((scores >= 60) & (scores < 75), axis=0)
D = np.sum((scores >= 50) & (scores < 60), axis=0)
F = np.sum(scores < 50, axis=0)

print("Grade Distribution (per subject)")
print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)
print("F:", F)
print()

# -------- (e) Correlation between subjects --------
corr_matrix = np.corrcoef(scores, rowvar=False)

print("Correlation Matrix:")
print(corr_matrix)