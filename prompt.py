def report_count(corpus):
    word_count = {}
    corpus = corpus.split()
    for word in corpus:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count