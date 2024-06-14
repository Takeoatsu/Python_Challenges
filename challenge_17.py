from itertools import repeat

def all_equals(equals):
    result = all(map(lambda x: x == equals[0], equals))
    return result

print(all_equals([1, 1, 1, 0]))
