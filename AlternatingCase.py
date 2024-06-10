def to_alternating_case(string):
    s = ""
    for x in string:
        if x == x.upper():
            x = x.lower()
            s += x
        elif x == x.lower():
            x =x.upper()
            s += x
    return s
