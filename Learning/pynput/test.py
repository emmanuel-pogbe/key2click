
def tuplify(str: str) -> tuple:
    cleaned = str.strip("() ").split(",")    
    return tuple(int(x) for x in cleaned)
x = "(6969,    1)"
y = tuplify(x)
print(sum(y))

