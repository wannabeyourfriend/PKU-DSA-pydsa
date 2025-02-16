from pythonds.basic.stack import Stack
# 简单括号匹配问题(判断是否是合式括号)

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close) # 根据值反索引

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol not in "([{)]}":
            index = index + 1
            continue
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1  
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
print(parChecker('{(d){f}}()'))