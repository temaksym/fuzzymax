from fuzzy_max import FuzzyMatcher

matcher = FuzzyMatcher(threshold=0.85, accurate_digits=True, case_sensitive=False)

print("\n")
print(["World War I", "World War II"], matcher.get_similarity("World War I", "World War II"), matcher.match("World War I", "World War II")) 
print(["E505", "E505"], matcher.get_similarity("E505", "E505"), matcher.match("E505", "E505")) 
print(["E504", "E505"], matcher.get_similarity("E504", "E505"), matcher.match("E504", "E505")) 


word_list = ["E505", "E423", "Almond", "gluten"]
text = '''
        Ingredients: Water, Sugar, Corn Syrup, High Fructose Corn Syrup, Apple Juice Concentrate, 
        Citric Acid, Natural Flavors, Sodium Benzoate (Preservative), Potassium Sorbate (Preservative), Almond
        E304, E670, E504, E4233, E763
        '''
matches = matcher.find_matches(word_list, text)
print("\n")
print("Matches in text: \n", matches)