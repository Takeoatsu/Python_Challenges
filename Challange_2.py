def mid(word):
    middle = int(len(word)/2)
    if len(word)%2 ==0:
        return ""
    else:
        return word[middle]

print(mid("abcd"))
    