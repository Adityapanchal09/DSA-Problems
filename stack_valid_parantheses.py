s="([{}])"
#output=True

def valid_parentheses(s):
    stack=[]

    matches={
        ")":"(",
        "}":"{",
        "]":"["
    }

    for char in s:
        if char in matches:
            if stack and stack[-1]==matches[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return len(stack)==0                


print(valid_parentheses(s))