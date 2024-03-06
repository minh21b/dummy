def report_count(corpus, token):
    word_count = {}
    for word in corpus:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count.get(token)