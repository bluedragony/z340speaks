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
def get_parts_of_speech_tags(sentence):
  
  ''' Returns Parts of Speech for words in the given sentence
  Input: Sentence separated by spaces
  Output: List of tuples where each tuple = \(word, tag\)'''

  if sentence == '':
    print ('Not a valid sentence.')
    return 

  if len(sentence) - sentence.count(' ') > 136:
    print ('Sum of letters in the sentence should be less than or equal to 136.')
    return
  
  import nltk
  words = sentence.split(" ")
  tags = nltk.pos_tag(words)
  word_tag = []

  for word,tag in tags:
    if 'NN' in tag:
      # Combining Nouns NNP/NNS/NNPS/NN
      word_tag.append((word,"NN"))
    elif 'DT' in tag:
      # Combining Determiner DT/PDT/WDT
      word_tag.append((word,"DT"))
    elif 'JJ' in tag:
      # Combining Adjectives JJR/JJS
      word_tag.append((word,"JJ"))
    elif 'PR' in tag or 'WP' in tag:
      # Combining Pronouns PRP/PR$/WP/WP$
      word_tag.append((word,"PR"))
    elif 'RB' in tag:  
      # Combining Adverbs RB/RBR/RBS/WRB
      word_tag.append((word,"RB"))
    elif 'VB' in tag:  
      # Combining Verbs VBG/VBD/VBN/VBP/VBZ
      word_tag.append((word,"VB"))
    elif 'IN' in tag or 'TO' in tag:  
      # Combining Preposition or TO
      word_tag.append((word,"IN")) 
    else:
      # Conjunctions, cardinals, existential, foreign word, list item marker
      # Modal auxiliary, particle (not participle), interjection
      word_tag.append((word,tag[:2])) 
  return word_tag

