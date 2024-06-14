def double_letters(text1):
    for i in range(len(text1)):
        if i != 0:
            if text1[i].lower() == text1[i-1].lower():
                return True
    return False

print(double_letters("Aaron"))
    