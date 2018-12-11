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
       filename - string type path of the input file
       
       **assuming the text is lower cased and no punctuations or special characters
       
       returns an output file "word_salad.txt" 
       Randomly shuffled words of the given input file text
       Split the words using whitespace as delimiter. 
       Randomly shuffles the list of words in place.
       Finally joins all the words with ' ' space 
       
      
    """
    
    def generate(self, file_name):
        with open(file_name, 'r') as file:
            text = file.read().replace('\n', ' ')

        random.seed(self.random_state)
        words = text.split()
        random.shuffle(words)
        word_salad = ' '.join(words)

        f = open("word_salad.txt", "a")
        f.write(word_salad)
