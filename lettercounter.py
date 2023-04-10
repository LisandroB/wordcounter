def letterCounter(word):
    dict = {};
    for letter in word:
        dict[letter] = word.count(letter)
    return dict;