def isValid(s: str) -> bool:
    left_Parentheses =[ '[','(' ,'{']
    right_Parentheses = [']',')', '}']
    stack = []
    for i in s:
        if i in left_Parentheses:
            stack.append(i)
        elif i in right_Parentheses:
            if not stack or not  1<= ord(i)-ord(stack[-1]) <= 2:
                return False
            stack.pop()
        else:
            return False
    return not stack
print(isValid(s= "[{()}]"))