#!/usr/bin/python3

import heapq
import sys

sys.setrecursionlimit(10000)

class DS:
    def __init__(self, x, y, state, fx):
        self.x = x
        self.y = y
        self.state = state
        self.fx = fx
    
    def __lt__(self, other):
        return self.fx < other.fx


def misplaceCount(state):
    m = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                m += 1
    return m

def swap(x1,y1,x2,y2,curr):
    cpy = [[j for j in i] for i in curr]
    cpy[x1][y1], cpy[x2][y2] = cpy[x2][y2], cpy[x1][y1]
    return cpy


def dfs(x, y, curr, goal, vis, res, depth):
    vis.append(curr)
    if curr == goal:
        for i in res:
            for j in i:
                print(*j)
            print()
        exit(0)

    pq = []
    for i in range(4):
        x1 = x + xMoves[i]
        y1 = y + yMoves[i]

        if 0<=x1<3 and 0<=y1<3:
            newState = swap(x,y,x1,y1,curr)
            if newState not in vis:
                fx = depth + misplaceCount(newState)
                heapq.heappush(pq, DS(x1, y1, newState, fx))
    while pq:
        root = heapq.heappop(pq)
        dfs(root.x, root.y, root.state, goal, vis, res + [root.state], depth+1)

    


curr = [[1,2,3],[None,4,6],[7,5,8]]
# goal = [[1,2,3],[4,5,6],[7,8,None]]
# goal = [[1,2,3],[4,5,6],[None,7,8]]
goal = [[1,3,None],[4,2,6],[7,5,8]]

vis = []
xMoves = [0,0,1,-1]
yMoves = [1,-1,0,0]
dfs(1, 0, curr, goal, vis, [], 0)
