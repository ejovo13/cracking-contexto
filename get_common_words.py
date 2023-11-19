"""Script to get a list of words using various NLTK corpora.

Generated using ChatGPT, modified by hand.
"""

import nltk
from nltk.corpus import stopwords, words

# Download NLTK resources (if not already downloaded)
nltk.download("brown")
nltk.download("stopwords")

# Get words from the Brown Corpus
# brown_words = brown.words()
words = words.words()


# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Calculate word frequencies
# freq_dist = FreqDist(filtered_words)

# print(freq_dist[0:100])


# Get the top x words
# top_x_words = freq_dist.most_common(150 * 1000)

# print(top_x_words[1:100])

print(len(filtered_words))

# # Print the top x words
file_name = "word_list_words.txt"

# with open(file_name, "w") as words:
#     for word_tuple in top_x_words:
#         word, _ = word_tuple

#         words.write(f"{word}\n")

with open(file_name, "w") as file:
    lines = [f"{w}\n" for w in filtered_words]
    file.writelines(lines)
