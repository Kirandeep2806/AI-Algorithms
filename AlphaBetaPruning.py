#!/usr/bin/python3

import math

arr = [3,5,2,9,12,5,23,23]
n = int(math.log2(len(arr)))

def alphaBeta(node, alpha, beta, depth):
    if depth == n:
        return arr[node]
    
    if depth&1:
        val = float("inf")
        for i in range(1,3):
            val = min(alphaBeta(node*2+i, alpha, beta, depth+1), val)
            alpha = min(alpha, val)
            if alpha >= beta:
                break
    else:
        val = -float("inf")
        for i in range(1,3):
            val = max(alphaBeta(node*2+i, alpha, beta, depth+1), val)
            beta = max(beta, val)
            if alpha >= beta:
                break
    return val
        

res = alphaBeta(0,-float("inf"),float("inf"),1)
print(res)
