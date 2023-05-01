#!/usr/bin/python3

class NQueens:
    def __init__(self):
        self.res = []
    
    def isSafe(self,n,row,col,arr):
        for i in range(row):
            if arr[i][col] == "Q":
                return False
        r = row-1
        c = col-1
        while r>=0 and c>=0:
            if arr[r][c]=="Q":
                return False
            r -= 1
            c -= 1
        r = row-1
        c = col+1
        while r>=0 and c<n:
            if arr[r][c] == "Q":
                return False
            r -= 1
            c += 1
        return True


    def solve(self,n,row,arr):
        if row == n:
            self.res.append([[i for i in j] for j in arr])
            return
        
        for col in range(n):
            if self.isSafe(n,row,col,arr):
                arr[row][col] = "Q"
                self.solve(n,row+1,arr)
                arr[row][col] = "."

    def NQueen(self,n):
        arr = [["."]*n for i in range(n)]
        self.solve(n,0,arr)
        for i in self.res:
            for j in i:
                print(*j)
            print("\n")

n = NQueens().NQueen(6)
