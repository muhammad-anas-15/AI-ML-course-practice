# Ultimate Word Frequency Analyzer

text = """
The history of Artificial Intelligence began in the mid-20th century, 
notably with Alan Turing's exploration of machine intelligence and 
the 1956 Dartmouth Workshop where the term "AI" was first coined. 
Early research focused on symbolic logic and problem-solving, but 
the field faced several "AI winters" due to limited computing power 
and high expectations. The trajectory shifted dramatically in the 2010s 
with the rise of Big Data and Deep Learning, leading to the sophisticated 
neural networks we use today. This evolution transformed AI from a theoretical 
concept into a practical tool integrated into modern communication and education.
"""

# stop words
stop_words = ['the','a','an','is','in','to','and','of','for','it','on','that','with','was']

# lowercase
clean = text.lower()

# remove punctuation
for ch in ",.!?":
    clean = clean.replace(ch, "")

# split text into list of words
words = clean.split()

# total words
total_words = len(words)

# count sentences
sentences = text.count(".") + text.count("!") + text.count("?")

# unique words, set() will remove duplicates
unique_words = len(set(words))

# create dictionary for frequencies
frequency = {}

for word in words:
    if word not in stop_words:
        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1

# top 10 most frequent words
top_10_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:10]

# longest and shortest words
longest = max(words, key=len)
shortest = min(words, key=len)

# average word length
total_len = 0

for w in words:
    total_len += len(w)

avg_len = total_len / total_words

# results
print("Total Words:", total_words)
print("Total Sentences:", sentences)
print("Unique Words:", unique_words)
print("Longest Word:", longest)
print("Shortest Word:", shortest)
print("Average Word Length:", round(avg_len,2))

print("\nTop 10 Frequent Words:")
for word, count in top_10_words:
    print(word, ":", count)

# bar chart
print("\nWord Frequency Chart:")
for word, count in top_10_words:
    print(word, "#"*count)