from difflib import SequenceMatcher
import re

class FuzzyMatcher:
    '''
    ## Class to match words based on similarity score.
    
    ### Attributes:
        threshold: float, the minimum similarity score to consider a match.
        accurate_digits: bool, if True, only consider a match if both words have the same digits.
        case_sensitive: bool, if True, consider case when matching words.
    ### Methods:
        set_threshold: set the threshold attribute.
        get_threshold: get the threshold attribute.
        set_accurate_digits: set the accurate_digits attribute.
        get_accurate_digits: get the accurate_digits attribute.
        match: return True if the similarity score between two words is greater than or equal to the threshold.
        get_similarity: return the similarity score between two words.
        find_best_match: return the best match for a word in a list of words.
        find_matches: return a list of best matches for a list of words in a text.
    '''
    def __init__(self, threshold=0.8, accurate_digits=True, case_sensitive=False):
        self.threshold = threshold
        self.accurate_digits = accurate_digits
        self.case_sensitive = case_sensitive

    def set_threshold(self, threshold):
        ''' Set the threshold attribute. '''
        self.threshold = threshold

    def get_threshold(self):
        ''' Get the threshold attribute. '''
        return self.threshold

    def set_accurate_digits(self, accurate_digits):
        ''' Set the accurate_digits attribute. '''
        self.accurate_digits = accurate_digits
    
    def get_accurate_digits(self):
        ''' Get the accurate_digits attribute. '''
        return self.accurate_digits

    def match(self, word1, word2):  
        ''' Returns True if the similarity score between two words is greater than or equal to the threshold. '''
        return self.get_similarity(word1, word2) >= self.threshold

    def get_similarity(self, word1, word2):
        ''' 
        Returns the similarity score between two words.
        If accurate_digits is True, only consider a match if both words have the same digits.
        '''
        if self.accurate_digits:
            if any(char.isdigit() for char in word1) or any(char.isdigit() for char in word2):
              if any(char.isdigit() for char in word1) and any(char.isdigit() for char in word2):
                if ''.join(filter(str.isdigit, word1)) != ''.join(filter(str.isdigit, word2)):
                  return 0.0
        return similarity_score(word1, word2)

    def find_best_match(self, word, word_list):
        ''' 
        ## Return the best match for a word in a list of words. 
        ### Input:
            word: str, the word to find a match for.
            word_list: list, a list of words to search for a match.
        ### Output:
            str, the best match for the word in the word
        '''
        if not self.case_sensitive:
            word_list = [word.lower() for word in word_list]
            word = word.lower()
    
        best_match = None
        highest_similarity = 0
        for candidate in word_list:
            similarity = similarity_score(word, candidate)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = candidate
        if highest_similarity >= self.threshold:
            return best_match
        return None


    def find_matches(self, word_list, text, indexes=False):
        '''
        ## Return a list of best matches for a list of words in a text.
        ### Input:
            word_list: list, a list of words to search for a match.
            text: str, the text to search for the words.
            indexes: bool, if True, return the indexes of the matches in the text.
        ### Output:
            list, a list of best matches for the words in the text.
        '''
        matches = []
        for word in tokenize(text):
            best_match = self.find_best_match(word, word_list)
            if indexes:
                matches.append([text.index(word), best_match])
            else:
                matches.append(best_match)
        return [match for match in matches if match]

def tokenize(text):
    ''' ## Tokenize a text into words. '''
    return re.findall(r'\b\w+\b', text)


def similarity_score(word1, word2):
    ''' ## Return the similarity score between two words. '''
    return SequenceMatcher(None, word1, word2).ratio()
