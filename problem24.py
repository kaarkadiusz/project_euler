def Permutation(s:str,  myList:list, prefix: str = ""):
    if s == "" or s == None:
        myList.append(prefix)
    
    for i in range(len(s)):
        Permutation(s[:i] + s[i+1:], myList, prefix + s[i])

permutations = []
Permutation("0123456789", permutations)

print(permutations[999999])