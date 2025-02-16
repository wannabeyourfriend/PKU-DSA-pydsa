# 01背包问题DP解法
tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]
max_w = 20
m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}

for i in range(1, len(tr)):
    for w in range(1, max_w + 1):
        if tr[i]['w'] > w:
            m[(i, w)] = m[(i - 1, w)]
        else:
            m[(i, w)] = max(m[(i - 1, w)], m[(i - 1, w - tr[i]['w'])] + tr[i]['v'])

# print(m[(len(tr) - 1, max_w)])

# 01背包问题递归解法
sr = {(2, 3),  (3, 4), (4, 8), (5, 8), (9, 10)}
max_w  =20
m = {}
def thief(sr, w):
    if sr == set() or w == 0:
        m[tuple(sr), w] = 0
        return 0
    elif (tuple(sr), w) in m:
        return m[tuple(sr), w]
    else:
        vmax = 0
        for s in sr:
            if s[0] <= w:
                v = thief(sr - {s}, w - s[0]) + s[1]
                vmax = max(vmax, v)
        m[tuple(sr), w] = vmax
        return vmax

print(thief(sr, max_w))