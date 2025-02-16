# 变位词的判断问题

# Solustion 1: 逐字符检查
def anagramSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 = pos1 + 1

    return stillOK

# example
print(anagramSolution1('abcd', 'dcba'))
# complexity: O(n^2)

# solution 2 排序检查 
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    if len(s1) != len(s2):
        matches = False
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches

# example
print(anagramSolution2('abcde', 'edcbfa'))

# complexity: O(nlogn)

# solution 3 暴力枚举：对s1的所有字符的排列进行枚举，然后检查是否有s2
def permute(s):
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s]
        res = []
        for i in range(len(s)):
            for p in permute(s[:i] + s[i + 1:]):
                res.append(s[i] + p)
        return res

def anagramSolution3(s1, s2):    
    return s2 in permute(s1)

# example
print(anagramSolution3('abc', 'bcda'))
# complexity: O(n!)

# solution 4 计数检查
def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False
    return stillOK

# example
print(anagramSolution4('apple', 'pleap'))
# complexity: O(n)  