#!/usr/bin/python3

REWARD = -0.01
DISCOUNT = 0.99
MAX_ERROR = 10**(-3)
ACTIONS = [(-1,0),(0,1),(1,0),(0,-1)]
DIRECTIONS = 4
NUM_ROWS = 3
NUM_COLS = 4
V = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0]]

COMPASS = {0: "UP", 1: "RIGHT", 2: "DOWN", 3: "LEFT"}

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
    print("\nDuring Iteration values are : \n")
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
        PrintEnvironment(V)
        print()
        if err < MAX_ERROR * (1-DISCOUNT) / DISCOUNT:
            break
    return V

def PrintEnvironment(V, policy=False):
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
                    if not policy:
                        print(str(V[r][c]).ljust(6))
                    else:
                        nextDirection = "RIGHT"
                        m = -float("inf")
                        for i in range(DIRECTIONS):
                            dr, dc = ACTIONS[i]
                            newR = r + dr
                            newC = c + dc
                            if newR<0 or newC<0 or newR>=NUM_ROWS or newC>=NUM_COLS:
                                continue
                            if V[newR][newC] >= m:
                                m = V[newR][newC]
                                nextDirection = COMPASS[i]
                        print(nextDirection.ljust(6))
            else:
                if not policy:
                    print(str(V[r][c]).ljust(6), end=" | ")
                else:
                    nextDirection = "RIGHT"
                    m = -float("inf")
                    for i in range(DIRECTIONS):
                        dr, dc = ACTIONS[i]
                        newR = r + dr
                        newC = c + dc
                        if newR<0 or newC<0 or newR>=NUM_ROWS or newC>=NUM_COLS:
                            continue
                        if V[newR][newC] >= m:
                            m = V[newR][newC]
                            nextDirection = COMPASS[i]
                    print(nextDirection.ljust(6), end=" | ")


print("Initial Environment : \n")
PrintEnvironment(V, policy=False)
V = ValueIteration(V)

print("\nOptimal Policy : \n")
PrintEnvironment(V, policy=True)
