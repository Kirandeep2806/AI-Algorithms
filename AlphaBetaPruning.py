#!/usr/bin/python3

import math

arr = [3,5,2,9,12,5,23,23]
n = int(math.log2(len(arr)))

def alphaBeta(node, alpha, beta, depth):
    if depth == n:
        return arr[node]
    
    if not depth&1:
        val = -float("inf")
        for i in range(2):
            val = max(alphaBeta(node*2+i, alpha, beta, depth+1), val)
            alpha = max(alpha, val)
            if alpha >= beta:
                break
    else:
        val = float("inf")
        for i in range(2):
            val = min(alphaBeta(node*2+i, alpha, beta, depth+1), val)
            beta = min(beta, val)
            if alpha >= beta:
                break
    return val
        

res = alphaBeta(0,-float("inf"),float("inf"),0)
print(res)
