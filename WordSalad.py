import random


class WordSaladGeneration:
    random_state = None

    """WordSaladGeneration
    
       init:
       random_state - an integer number to give as a seed to random number generator (default = 1)
       
       **for a given random_state we always get the same output
       **if we change the random state we will get a different output
    """
    def __init__(self, random_state=1):
        self.random_state = random_state

    """Form a complex number.

       generate:
       text - a string value
       
       **assuming the text is lower cased 
       
       returns randomly shuffled words of the given text
       Split the words using whitespace as delimiter. 
       Randomly shuffles the list of words in place.
       Finally joins all the words with ' ' space 
       
      
    """
    def generate(self, text):
        random.seed(self.random_state)
        words = text.split()
        random.shuffle(words)
        word_salad = ' '.join(words)
        return word_salad
