temps=[73,74,75,71,69,72,76,73]

def temperature_rise(temps):
    n=len(temps)
    stack=[]
    result=[0]*n


    for i,temp in enumerate(temps):
        while stack and temps[stack[-1]]<temp:
                prev_index=stack.pop()
                result[prev_index]=i-prev_index
        stack.append(i)
    return result            


print(temperature_rise(temps))


#time=O(n)(each index pushed once and popped at most once)
#space-O(n)(space for stack in worst case(nothing ever pops in strictly decreasing temperatures))
