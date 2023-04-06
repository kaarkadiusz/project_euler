def GetCycleLength(n: int):
    stateToIter = {}
    state = 1
    iter = 0
    while(state not in stateToIter):
        stateToIter[state] = iter
        state = state * 10 % n
        iter += 1
    return iter - stateToIter[state]

bestNumber = 0
bestLength = 0
for i in range (1, 1001):
    length = GetCycleLength(i)
    if length > bestLength:
        bestNumber = i
        bestLength = length
        
print(f"{bestNumber} : {bestLength}")