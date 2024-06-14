def palindrome(word):
    normal = []
    
    for letters in word:
        normal.append(letters)
    
    pali = normal[::-1]
    
    if pali == normal:
        return True
    else:
        return False
        
print(palindrome("appa"))
        