"""Script to get a list of the n most common words in the Brown corpus.

Generated using ChatGPT
"""

import nltk
from nltk import FreqDist
from nltk.corpus import brown
from nltk.corpus import stopwords

# Download NLTK resources (if not already downloaded)
nltk.download('brown')
nltk.download('stopwords')

# Get words from the Brown Corpus
brown_words = brown.words()

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in brown_words if word.lower() not in stop_words]

# Calculate word frequencies
freq_dist = FreqDist(filtered_words)

# Get the top x words
top_x_words = freq_dist.most_common(50000)  # Change 10000 to your desired number

# Print the top x words
file_name = "nltk_common_words.txt"

with open(file_name, "w") as words:
    for word_tuple in top_x_words:
        word, _ = word_tuple

        words.write(f"{word}\n")
