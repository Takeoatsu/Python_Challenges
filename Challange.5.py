import math

def only_ints(value1, value2):
    if type(value1) is int and type(value2) is int:
        return True
    else: 
        return False

print (only_ints(3,True))