def validate(string):
    
    val = True
    
    if "def" not in string:
        return "missing def"
    if ":" not in string:
        return "missing :"
    if "(" and ")" not in string:
        return "missing paren"
    if "(" + ")" in string:
        return "missing param"
    if "    " not in string:
        return "missing indent"
    if "validate" not in string:
         return "wrong name"
    if "return" not in string:
        return "missing return"
    
    return val

