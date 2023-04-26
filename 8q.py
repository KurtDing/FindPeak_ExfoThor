def conflict(state, nextX):    
    nextY = len(state)
    return any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))

def queens(n, state=()):
    if len(state) == n: 
        return [()]
    ans = []
    for pos in range(n):
        if not conflict(state, pos):
            for result in queens(n, state + (pos,)):
                ans += [(pos,)+ result ]
            print('POS:', pos, 'Try:', ans)
    return ans

print(queens(4))
