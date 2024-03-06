def report_count(corpus, token):
    word_count = {}
    for word in corpus:
        word_count[word] = word_count.get(word, 0) + 1
    count = word_count.get(token)
    return count