target=10
position=[1,4]
speed=[3,2]
#output=1



def fleet(target,position,speed):
    stack=[]
    cars=sorted(zip(position,speed),reverse=True)

    for pos,spd in cars:
        time=(target-pos)/spd

        if not stack  or time>stack[-1]:
            stack.append(time)
    return len(stack)

print(fleet(target,position,speed))

#time=O(n log n)-sorting(O(n log n)) dominates on for loop(O(n))
#space=O(n)-(in sorting formed a new list of tuples O(n) and at worst case O(n) if all cars are slower than one ahead)



    

