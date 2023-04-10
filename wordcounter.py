def wordCounter(phrase):
    dict = {};
    words = phrase.split()
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict