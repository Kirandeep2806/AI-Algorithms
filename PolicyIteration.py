import random

REWARD = -0.01
DISCOUNT = 0.99
MAX_ERROR = 10**(-3)
ACTIONS = [(-1,0),(0,1),(1,0),(0,-1)]
COMPASS = {0: "UP", 1: "RIGHT", 2: "DOWN", 3: "LEFT"}
DIRECTIONS = 4
NUM_ROWS = 3
NUM_COLS = 4
V = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0]]

policy = [[random.randint(0,3) for _ in range(NUM_COLS)] for __ in range(NUM_ROWS)]

def GetV(V, r, c, action):
    dr, dc = ACTIONS[action]
    r += dr
    c += dc
    if r<0 or c<0 or r>=NUM_ROWS or c>=NUM_COLS or (r==c==1):
        return V[r-dr][c-dc]
    return V[r][c]

def CalculateV(V, r, c, action):
    v = REWARD
    v += 0.1 * DISCOUNT * GetV(V, r, c, (action-1)%4)
    v += 0.8 * DISCOUNT * GetV(V, r, c, action)
    v += 0.1 * DISCOUNT * GetV(V, r, c, (action+1)%4)
    return v

def PolicyEvaluation(policy, V):
    while True:
        VDash = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0]]
        err = 0
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if r==c==1 or (r<=1 and c==3):
                    continue
                VDash[r][c] = round(CalculateV(V, r, c, policy[r][c]), 3)
                err = max(err, abs(VDash[r][c] - V[r][c]))
        V = VDash
        if err < MAX_ERROR * (1-DISCOUNT) / DISCOUNT:
            break
    return V

def PolicyIteration(policy, V):
    print("\nDuring Updations : ")
    latestV = V
    while True:
        V = PolicyEvaluation(policy, V)
        unchanged = True
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if r==c==1 or (r<=1 and c==3):
                    continue
                maxAction, maxV = None, -float("inf")
                for action in range(DIRECTIONS):
                    v = CalculateV(V, r, c, action)
                    if v > maxV:
                        maxAction, maxV = action, v
                if maxV > CalculateV(V, r, c, policy[r][c]):
                    policy[r][c] = maxAction
                    unchanged = False
        if unchanged:
            break
        print()
        PrintEnvironment(V)
        latestV = V
    return latestV


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


print("The initial random policy is:\n")
PrintEnvironment(policy)
V = PolicyIteration(policy, V)
print("\nThe optimal policy is:\n")
PrintEnvironment(V, True)
