# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Create an empty list to store the matching anagrams
        matches = []

        # Convert the word to lowercase and sort its letters
        sorted_word = sorted(self.word.lower())

        # Iterate over the word_list and compare each word
        for candidate in word_list:
            # Convert the candidate word to lowercase and sort its letters
            sorted_candidate = sorted(candidate.lower())
            
            # Check if the sorted letters of the candidate word match the sorted letters of the original word
            if sorted_candidate == sorted_word and candidate.lower() != self.word.lower():
                matches.append(candidate)

        return matches
