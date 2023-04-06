def StringPlusString(s1: str, s2: str) -> str:
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    
    s2 = "".join("0" for _ in range(len(s1) - len(s2))) + s2
    
    carry = 0
    result = ""
    for a, b in zip(reversed(s1), reversed(s2)):
        suma = int(a) + int(b) + carry
        carry = suma // 10
        result += str(suma % 10)
        
    result += str(carry) if carry != 0 else ""
    
    return result[::-1]

def StringTimesString(s1: str, s2:str) -> str:
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    
    multiplication_list = []
    current_power_of10 = 0
    for b in reversed(s2):
        carry = 0
        multiplication_result = ""
        for a in reversed(s1):
            product = int(b) * int(a) + carry
            carry = product // 10
            multiplication_result += str(product % 10)
        multiplication_result += str(carry) if carry != 0 else ""
        multiplication_result = "".join("0" for _ in range(current_power_of10)) + multiplication_result
        multiplication_list.append(multiplication_result[::-1])
        current_power_of10 += 1
    
    result = ""
    for i in multiplication_list:
        result = StringPlusString(result, i)
    
    return result