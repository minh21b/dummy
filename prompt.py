def report_count(token):
    return word_count.get(token)

def word_count(data):
    word_count = {}
    data = data.split()
    for word in data:
        word_count[word] = word_count.get(word, 0) + 1
    #token = token
    return word_count