# Peshawari Restaurant Review Analyzer

reviews = [
"The food was delicious and the service was excellent. I love this place.",
"The taste was terrible and the service was bad.",
"Amazing food and wonderful atmosphere. Best restaurant in town.",
"The meal was awful and the waiter was horrible.",
"Great taste and fantastic presentation.",
"The food was disgusting and the place looked poor.",
"I love the delicious biryani here.",
"The experience was bad but the food was good.",
"Excellent service and amazing taste.",
"The worst restaurant ever, horrible service.",
"Fantastic flavors and great hospitality.",
"The food was okay but nothing special.",
"Wonderful dishes and I love the desserts.",
"The soup tasted awful and the meal was poor.",
"Best kebabs ever, absolutely delicious."
]

positive_words = ["delicious","amazing","excellent","great","best","fantastic","wonderful","love"]
negative_words = ["terrible","awful","bad","worst","disgusting","horrible","poor","hate"]

pos_freq = {}
neg_freq = {}

results = []

for i, review in enumerate(reviews, 1):

    text = review.lower()

    for ch in ".,!":
        text = text.replace(ch, "")

    words = text.split()

    pos_count = 0
    neg_count = 0

    for w in words:
        if w in positive_words:
            pos_count += 1
            pos_freq[w] = pos_freq.get(w,0) + 1

        if w in negative_words:
            neg_count += 1
            neg_freq[w] = neg_freq.get(w,0) + 1

    total = pos_count + neg_count

    if total == 0:
        score = 0
    else:
        score = (pos_count - neg_count) / total

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    results.append((i,pos_count,neg_count,round(score,2),sentiment))


# most common words
most_pos = max(pos_freq, key=pos_freq.get)
most_neg = max(neg_freq, key=neg_freq.get)

# write to file
with open("review_analysis.txt","w") as f:

    f.write("Peshawari Restaurant Review Analysis\n")
    f.write("="*45 + "\n\n")

    f.write("Review | Pos | Neg | Score | Sentiment\n")
    f.write("-"*45 + "\n")

    for r in results:
        f.write(f"{r[0]:6} | {r[1]:3} | {r[2]:3} | {r[3]:5} | {r[4]}\n")

    f.write("\nMost Common Positive Word: " + most_pos)
    f.write("\nMost Common Negative Word: " + most_neg)

print("Analysis saved to review_analysis.txt")