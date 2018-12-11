from WordSalad import WordSaladGeneration


if __name__ == '__main__':

    text = "generated a sample text to get a randomly shuffled text which is a word salad"
    ws = WordSaladGeneration(19)
    print(ws.generate(text))
