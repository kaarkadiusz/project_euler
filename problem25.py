import problemsmodule as pm

previousTerm, currentTerm = "0", "1"

print(f"0: {previousTerm}")
print(f"1: {currentTerm}")
i = 2
while len(currentTerm) != 1000:
    currentTerm, previousTerm = pm.StringPlusString(previousTerm, currentTerm), currentTerm
    print(f"{i}: {currentTerm}")
    i+=1