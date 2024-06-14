def add_dots(text1):
   word = ".".join(text1)
   return word

print(add_dots("test"))

def remove_dots(text2):
    word = text2
    remove = word.replace(".",'')
    return remove

print(remove_dots("t.e.s.t"))

