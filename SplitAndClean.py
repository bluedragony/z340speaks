
# coding: utf-8

# # split_with_space(inputFilePath,outputFilePath, splitLength) - 

# Function to return a splitted 136 character file at outputFilePath provided

# In[75]:


def split_with_space(inputFilePath,outputFilePath, splitLength):    
    with open(inputFilePath, 'r') as f:          # filePath = 'alice_oz.txt', splitLength = 136
        textData = f.read()                   
    #print(textData)
    textEach = ""                         # initialize
    textWordCount = 0                  # initialize      
    textWords = textData.split(" ")        # All words in the text
    for word in textWords:
        if(word!= ""):            
            if((textWordCount + len(word))<splitLength):    # check if the new word added does not make length >136. If it does, we exclude it
                textEach = textEach + " "+ word
                textWordCount = textWordCount + len(word)
            else:
                with open(outputFilePath, 'a+') as f:     #outputFilePath = 'newFile.txt'
                    f.write(textEach)
                    f.write('\n')
                textEach = word          # reset for the next line
                textWordCount = len(word)   # reset for the next line
    print("text each is: ",textEach)
    if(textEach!=""):
        with open(outputFilePath, 'a+') as f:     #outputFilePath = 'newFile.txt'
            f.write(textEach)
            f.write('\n')

split_with_space('alice_oz.txt','newFile.txt',136)


# #  RemoveSpaces(inputFilePath,outputFilePath)

# returns without space file at the outputFilePath location 

# In[74]:


def RemoveSpaces(inputFilePath,outputFilePath):    
    with open(inputFilePath, 'r') as f:          # filePath = 'newFile.txt'
        textData = f.readlines()
    for t in textData:
        s = t.replace(' ', '')
        with open(outputFilePath, 'a+') as f:     #outputFilePath = 'finalWithotSpace.txt'
            f.write(s)
            f.write('\n')

RemoveSpaces('newFile_1.txt', "finalWithotSpace.txt")

