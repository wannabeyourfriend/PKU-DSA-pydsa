def toStr(n, base) -> str:
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]
    
print(toStr(1453, 16))