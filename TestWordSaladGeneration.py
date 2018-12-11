from WordSalad import WordSaladGeneration


if __name__ == '__main__':

    # 19 is a random seed
    ws = WordSaladGeneration(19)
    filename = "sample_test.txt"
    ws.generate(filename)
