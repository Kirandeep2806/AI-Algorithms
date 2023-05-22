#!/usr/bin/python3

REWARD = -0.01
DISCOUNT = 0.99
MAX_ERROR = 10**(-3)
ACTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
DIRECTIONS = 4
NUM_ROWS = 3
NUM_COLS = 4
V = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0]]

def GetV(V, r, c, action):
    dr, dc = ACTIONS[action]
    r += dr
    c += dc
    if r<0 or c<0 or r>=NUM_ROWS or c>=NUM_COLS or (r==1 and c==1):
        return V[r-dr][c-dc]
    return V[r][c]

def CalculateV(V, r, c, action):
    v = REWARD
    v += 0.1 * DISCOUNT * GetV(V, r, c, (action-1)%4)
    v += 0.8 * DISCOUNT * GetV(V, r, c, action)
    v += 0.1 * DISCOUNT * GetV(V, r, c, (action+1)%4)
    return v

def ValueIteration(V):
    while True:
        VDash = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0]]
        err = 0
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if (r<=1 and c==3) or (r==1 and c==1):
                    continue
                cv = [CalculateV(V, r, c, action) for action in range(DIRECTIONS)]
                m = max(cv)
                VDash[r][c] = round(m, 4)
                err = max(err, VDash[r][c] - V[r][c])
        V = VDash
        if err < MAX_ERROR * (1-DISCOUNT) / DISCOUNT:
            break
    return V

def GetOptimalPolicy(V):
    policy = [[-1, -1, -1, -1] for _ in range(NUM_ROWS)]
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if (r<=1 and c==3) or (r==1 and c==1):
                continue
            maxAction, maxV = None, -float("inf")
            for action in range(DIRECTIONS):
                v = CalculateV(V, r, c, action)
                if v > maxV:
                    maxAction, maxV = action, v
            policy[r][c] = maxAction
    return policy

def PrintEnvironment(V):
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if r == 1 and c == 1:
                print("WALL".ljust(6), end=" | ")
            elif c == 3:
                if r <= 1:
                    if r == 0:
                        print("+1")
                    else:
                        print("-1")
                else:
                    print(str(V[r][c]).ljust(6))
            else:
                print(str(V[r][c]).ljust(6), end=" | ")

print("Initial Environment : \n")
PrintEnvironment(V)

V = ValueIteration(V)
res = GetOptimalPolicy(V)

print("\n\nOptimal Policy : \n")
PrintEnvironment(V)
