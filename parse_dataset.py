import os
import sys

import random
from nltk.util import ngrams


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

    def generate(self, in_file, out_file):
        random.seed(self.random_state)
        in_fh = open(in_file)
        out_fh = open(out_file, 'w')
        while True:
            line = in_fh.readline().replace('\n', ' ')
            if not line:
                break
            words = line.split()
            random.shuffle(words)
            word_salad = ' '.join(words) + '\n'
            out_fh.write(word_salad)
        out_fh.close()
        in_fh.close()


def split_with_space(inputFilePath, outputFilePath, splitLength):
    with open(inputFilePath, 'r') as f:  # filePath = 'alice_oz.txt', splitLength = 136
        textData = f.read()
    textEach = ""  # initialize
    textWordCount = 0  # initialize
    textWords = textData.split(" ")  # All words in the text
    for word in textWords:
        if (word != ""):
            if ((textWordCount + len(
                    word)) < splitLength):  # check if the new word added does not make length >136. If it does, we exclude it
                textEach = textEach + " " + word
                textWordCount = textWordCount + len(word)
            else:
                with open(outputFilePath, 'a+') as f:  # outputFilePath = 'newFile.txt'
                    f.write(textEach)
                    f.write('\n')
                textEach = word  # reset for the next line
                textWordCount = len(word)  # reset for the next line
    if (textEach != ""):
        with open(outputFilePath, 'a+') as f:  # outputFilePath = 'newFile.txt'
            f.write(textEach)
            f.write('\n')


def removes_all_spaces(inputFilePath, outputFilePath):
    with open(inputFilePath, 'r') as f:  # filePath = 'newFile.txt'
        textData = f.readlines()
    for t in textData:
        s = t.replace(' ', '')
        with open(outputFilePath, 'a+') as f:  # outputFilePath = 'finalWithotSpace.txt'
            f.write(s)
            # f.write('\n')


def remove_training_and_starting_spaces(in_file, out_file):
    in_fh = open(in_file)
    out_fh = open(out_file, 'w')
    while True:
        line = in_fh.readline()
        if not line:
            break
        line = line.lstrip().rstrip() + '\n'
        out_fh.write(line)
    out_fh.close()
    in_fh.close()


''' 
@authors:
neha.bhagwat@sjsu.edu
gayatri.gadre@sjsu.edu

Prerequisite:
Download the following packages:

nltk.download('brown')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')

'''


def process_POS(inFile, outFile):
    with open(outFile, 'w') as outFile:
        with open(inFile, "r") as f:
            content = f.readlines()
            pos = ""
            for line in content:
                line = line.rstrip().lstrip()
                # print(line)
                pos += (str([x[1] for x in get_parts_of_speech_tags(line)])[1:-1] + "\n")
                pos = pos.replace('\'', '').replace(',', '')
                # print(pos)
            outFile.write(str(pos))
    f.close()
    outFile.close()


def get_parts_of_speech_tags(sentence):
    ''' Returns Parts of Speech
    Input: Sentence separated by spaces
    Output: List of tuples where each tuple = \(word, tag\)'''

    if sentence == '':
        print('Not a valid sentence.')
        return []

    if len(sentence) - sentence.count(' ') > 136:
        print('Sum of letters in the sentence should be less than or equal to 136.')
        return []

    import nltk
    words = sentence.split(" ")
    tags = nltk.pos_tag(words)
    word_tag = []

    for word, tag in tags:
        if 'NN' in tag:
            # Combining Nouns NNP/NNS/NNPS/NN
            word_tag.append((word, "NN"))
        elif 'DT' in tag:
            # Combining Determiner DT/PDT/WDT
            word_tag.append((word, "DT"))
        elif 'JJ' in tag:
            # Combining Adjectives JJR/JJS
            word_tag.append((word, "JJ"))
        elif 'PR' in tag or 'WP' in tag:
            # Combining Pronouns PRP/PR$/WP/WP$
            word_tag.append((word, "PR"))
        elif 'RB' in tag:
            # Combining Adverbs RB/RBR/RBS/WRB
            word_tag.append((word, "RB"))
        elif 'VB' in tag:
            # Combining Verbs VBG/VBD/VBN/VBP/VBZ
            word_tag.append((word, "VB"))
        elif 'IN' in tag or 'TO' in tag:
            # Combining Preposition or TO
            word_tag.append((word, "IN"))
        else:
            # Conjunctions, cardinals, existential, foreign word, list item marker
            # Modal auxiliary, particle (not participle), interjection
            word_tag.append((word, tag[:2]))
    return word_tag


def process_n_grams(n, inFile, outFile):
    with open(outFile, 'w') as outFile:
        with open(inFile, "r") as f:
            content = f.readlines()
            n_gram = ""
            for line in content:
                line = line.rstrip().lstrip()
                n_gram_op = generate_n_grams(line, n)
                n_gram_op = [''.join(gram) for gram in n_gram_op]
                n_gram += str(n_gram_op).replace('\'', '').replace(',', '') + '\n'
            outFile.write(str(n_gram))
    f.close()
    outFile.close()


def generate_n_grams(text, n):
    # if you want word-grams and not character-grams: token = nltk.word_tokenize(text); n_grams = ngrams(token, n)
    n_grams = ngrams(text, n)
    return list(n_grams)


def main(argv):
    input_corpus_file = 'alice_oz.txt'
    english_text_136_with_spaces_file = 'english_text_136_with_spaces.txt'
    english_text_136_without_spaces_file = 'english_text_136_without_spaces.txt'
    pos_text_136_with_spaces_file = 'pos_text_136_with_spaces.txt'
    n_grams_136_english_text_file = 'n_grams_136_english_text.txt'

    junk1_file = 'junk1.txt'
    word_salad_136_with_spaces_file = 'word_salad_136_with_spaces.txt'
    word_salad_136_without_spaces_file = 'word_salad_136_without_spaces.txt'
    pos_word_salad_136_with_spaces_file = 'pos_word_salad_136_with_spaces.txt'
    n_grams_136_word_salad_file = 'n_grams_136_word_salad.txt'

    # remove these files to generate fresh
    file_list_to_delete = [english_text_136_with_spaces_file, english_text_136_without_spaces_file,
                           pos_text_136_with_spaces_file, junk1_file, word_salad_136_with_spaces_file,
                           pos_word_salad_136_with_spaces_file]

    for i in range(len(file_list_to_delete)):
        if os.path.exists(file_list_to_delete[i]):
            os.remove(file_list_to_delete[i])

    #
    # parse corpus and generate file with 136 len sequence
    split_with_space(input_corpus_file, junk1_file, 136)

    # remove trailing and starting spaces from file
    remove_training_and_starting_spaces(junk1_file, english_text_136_with_spaces_file)

    removes_all_spaces(english_text_136_with_spaces_file, english_text_136_without_spaces_file)

    #
    # remove trailing and starting spaces from file
    remove_training_and_starting_spaces(junk1_file, english_text_136_with_spaces_file)

    removes_all_spaces(english_text_136_with_spaces_file, english_text_136_without_spaces_file)
    removes_all_spaces(word_salad_136_with_spaces_file, word_salad_136_without_spaces_file)

    # parse file with 136 len sequence to generate POS
    process_POS(english_text_136_with_spaces_file, pos_text_136_with_spaces_file)

    # 19 is a random seed
    ws = WordSaladGeneration(19)
    ws.generate(english_text_136_with_spaces_file, word_salad_136_with_spaces_file)

    process_POS(word_salad_136_with_spaces_file, pos_word_salad_136_with_spaces_file)

    process_n_grams(7, english_text_136_without_spaces_file, n_grams_136_english_text_file)
    process_n_grams(7, word_salad_136_without_spaces_file, n_grams_136_word_salad_file)


if __name__ == "__main__":
    main(sys.argv)
