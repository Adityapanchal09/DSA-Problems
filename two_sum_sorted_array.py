#numbers=[1,2,3,4] target=3
#output=[1,2]

def twosum(numbers,target):
    left=0
    right=len(numbers)-1

    while left<right:
        current_sum=numbers[left]+numbers[right]

        if current_sum==target:
            return[left+1,right+1]
        elif current_sum < target:
            left+=1
        else:
            right-=1
    return []            
    

print(twosum([1,2,3,4],3))
print(twosum([2,7,11,15],9))
