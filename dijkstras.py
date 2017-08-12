import heapq
from collections import namedtuple, defaultdict

Node = namedtuple('Node', ['depth', 'index'])
disjoint = float('inf')


def AddAdjacent(heap, adjacency, node):
    row = node.index
    for col in xrange(len(adjacency[row])):
        if adjacency[row][col] == disjoint:
            continue
        depth = node.depth + adjacency[row][col]
        heapq.heappush(heap, Node(depth=depth, index=col))


def FindShortestDistanceBetween(adjacency, a, b):
    visited = defaultdict(lambda: False)
    curr = Node(depth=0, index=a)
    heap = [curr]

    while curr.index != b and heap:
        curr = heapq.heappop(heap)
        if visited[curr.index]:
            continue
        visited[curr.index] = True
        AddAdjacent(heap, adjacency, curr)
    if curr.index == b:
        return b.depth
    return disjoint
