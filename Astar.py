#!/usr/bin/python3

import heapq

class DS:
    def __init__(self, node, fx, dist):
        self.node = node
        self.dist = dist
        self.fx = fx

    def __lt__(self, other):
        return self.fx < other.fx


def dfs(cur, goal, distanceCovered, vis, res):
    global pq
    if cur == goal:
        print(' -> '.join(res))
        exit(0)
    
    vis[cur] = True
    for vals in Graph_nodes[cur]:
        if vals!=None:
            node, distance = vals
            if node not in vis:
                fx = distanceCovered + H_dist[node]
                heapq.heappush(pq, DS(node, fx, distance))
    while pq:
        ds = heapq.heappop(pq)
        dfs(ds.node, goal, distanceCovered + ds.dist, vis, res + [ds.node])

pq = []
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

H_dist = {
    'A': 11,
    'B': 1,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0,
}

start = "A"
goal = "G"

dfs(start, goal, 0, {}, ["A"])
