# 实现广度优先搜索策略
from pythonds.basic.queue import Queue
from pythonds.basic.graph import Graph


def bfs(graph, start):
    start.setDistance(0)
    start.setPredecessor(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPredecessor(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    while x.getPredecessor():
        print(x.id)
        x = x.getPredecessor()
    print(x.id)

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

def main():
    g = build_graph('fourletterwords.txt')
    start = g.getVertex('fool')
    end = g.getVertex('same')
    bfs(g, start)
    traverse(end)

main()