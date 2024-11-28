# FuzzyMax Project

## Team Members:
- Maksym Teutuliak
- Maksym Altukhov

## Project Description
FuzzyMax is a Python package designed to find the best matches for a list of words within a given text. It utilizes fuzzy matching techniques to identify the most similar words and provides options to return the indexes of these matches within the text.

## Main Functionality
- **find_matches(word_list, text, indexes=False)**: Returns a list of best matches for a list of words in a text. If `indexes` is set to `True`, it also returns the indexes of the matches in the text.
- **tokenize(text)**: Tokenizes a text into words.
- **similarity_score(word1, word2)**: Returns the similarity score between two words.

## Examples
```python
from fuzzymax import FuzzyMax

# Initialize FuzzyMax
fuzzymax = FuzzyMax()

# Define a list of words to search for
word_list = ["apple", "banana", "orange"]

# Define the text to search within
text = "I have an apple and a banana."

# Find matches
matches = fuzzymax.find_matches(word_list, text)
print(matches)  # Output: ['apple', 'banana']

# Find matches with indexes
matches_with_indexes = fuzzymax.find_matches(word_list, text, indexes=True)
print(matches_with_indexes)  # Output: [[11, 'apple'], [21, 'banana']]
