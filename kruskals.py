import heapq
from collections import namedtuple, defaultdict


class Node:

    def __init__(self, index):
        self.index = index
        self.parent = None
        self.rank = 0

    def findParent(self):
        if self.parent is None:
            return self
        self.parent = self.parent.findParent()
        return self.parent

Edge = namedtuple('Node', ['weight', 'a', 'b'])
disjoint = float('inf')


def AreConnected(nodes, a, b):
    return nodes[a].findParent().index == nodes[b].findParent().index


def Union(nodes, a, b):
    if AreConnected(nodes, a, b):
        return
    lesser = nodes[a].findParent()
    greater = nodes[b].findParent()
    if lesser.rank > greater.rank:
        lesser, greater = greater, lesser
    lesser.parent = greater
    if lesser.rank == greater.rank:
        greater.rank += 1


def FindMinimumSpanningTree(adjacent):
    nodes = map(Node, xrange(len(adjacent)))
    heap = []
    result = defaultdict(lambda: defaultdict(lambda: disjoint))

    for i in xrange(len(adjacent)):
        for j in xrange(len(adjacent[i])):
            if adjacent[i][j] != disjoint:
                heapq.heappush(heap, Edge(weight=adjacent[i][j], a=i, b=j))

    while heap:
        curr = heapq.heappop(heap)
        a, b = curr.a, curr.b
        if AreConnected(nodes, a, b):
            continue
        Union(nodes, a, b)
        result[a][b] = curr.weight
        result[b][a] = curr.weight

    return result
