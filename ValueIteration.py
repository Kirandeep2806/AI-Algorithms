actions = (0, 1)
states = (0, 1, 2, 3, 4)
rewards = [-1, -1, 10, -1, -5]
gamma = 0.9

prob = [
    [[0.9, 0.1], [0.1, 0.9], [0, 0], [0, 0], [0, 0]],
    [[0.9, 0.1], [0, 0], [0.1, 0.9], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0.9, 0.1], [0, 0], [0.1, 0.9]],
    [[0, 0], [0, 0], [0, 0], [0.9, 0.1], [0.1, 0.9]],
]

V = [0, 0, 0, 0, 0]
pi = [None, None, None, None, None]

while True:
    V_new = [0, 0, 0, 0, 0]
    for s in states:
        max_val = 0
        for a in actions:
            val = 0
            for s_next in states:
                val += prob[s][s_next][a] * V[s_next]
            val *= gamma
            val += rewards[s]
            max_val = max(max_val, val)
            if V[s] < val:
                pi[s] = a
        V_new[s] = round(max_val, 2)

    if V_new == V:
        break
    V = V_new

print("Best approach at each state :", V)
print("Optimal policy :", pi)
for i in range(len(pi)):
    if pi[i] == 1:
        pi[i] = "\u2192"
    if pi[i] == 0:
        pi[i] = "\u2190"
print("Optimal policy :", pi)
