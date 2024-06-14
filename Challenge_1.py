def capital_index(word):

    res = [idx for idx in range(len(word)) if word[idx].isupper()]

    return res

print(capital_index("HeLlO"))