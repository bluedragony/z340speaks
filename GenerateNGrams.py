import nltk
from nltk.util import ngrams


def generateNGrams(text, n):
    # if you want word-grams and not character-grams: token = nltk.word_tokenize(text); n_grams = ngrams(token, n)
    n_grams = ngrams(text, n)
    return list(n_grams)


def seven_grams(file_name):
    with open(file_name, 'r') as file:
        text = file.read().replace('\n', '')
    n = 7

    # text is assumed to have spaces and all spaces are removed
    text = text.replace(" ", "")
    n_grams = generateNGrams(text, n=n)
    f = open("7_grams_Alice_1.txt", "a")
    f.write(str(n_grams))


if __name__ == '__main__':
    # give file name here
    seven_grams("test_ngrams.txt")


