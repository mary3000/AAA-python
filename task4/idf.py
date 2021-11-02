import math


def idf_transform(words):
    idf = [0] * len(words[0])
    all_docs = len(words)
    for j in range(len(words[0])):
        docs_with_word = 0
        for i in range(len(words)):
            docs_with_word += (words[i][j] != 0)
        idf[j] = round(math.log((all_docs + 1) / (docs_with_word + 1)) + 1, 1)
    return idf
