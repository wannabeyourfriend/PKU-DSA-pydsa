# 使用图数据结构解决词梯问题
# 词梯问题：给定两个单词，找到从一个单词到另一个单词的最短序列，每次只能改变一个字母，且新单词必须在字典中
from pythonds.basic.graph import Graph
def build_graph(words):
    d = {}
    g = Graph()
    wfile = open(words, 'r')
    # 创建桶
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g