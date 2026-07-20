tokens=["1","2","+","3","*","4","-"]

def rpn_evaluation(tokens):
    stack=[]

    operators={
        "+":lambda a,b:a+b,
        "-":lambda a,b:a-b,
        "*":lambda a,b:a*b,
        "/":lambda a,b:int(a/b)
    }

    for token in tokens:
        if token in operators:
            right_operand=stack.pop()
            left_operand=stack.pop()

            result=operators[token](left_operand,right_operand)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack[0]



print(rpn_evaluation(tokens))