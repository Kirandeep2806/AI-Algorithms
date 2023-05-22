#!/usr/bin/python3

import math

arr = [3,5,2,9,12,5,23,23]
n = int(math.log2(len(arr)))

def minimax(node, depth):
    if depth == n:
        return arr[node]
    left = minimax(node*2, depth+1)
    right = minimax(node*2+1, depth+1)
    if depth&1:
        return min(left, right)
    else:
        return max(left, right)

print(minimax(0,0))
