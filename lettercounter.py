def letterCounter(word):
    list = 0;
    for letter in word:
        if letter == " ":
            continue;
        else:
            list+=1;
    return list;