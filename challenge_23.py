def list_xor(n, list1, list2):
    if n in list1:
        if n in list2:
            return False
        else: 
            return True
    else:
        if n in list2:
            return True
        else: 
            return False

print(list_xor(1, [1, 2, 3], [4, 5, 6]))