#return indexes of output whose sum are equal to the targer
#target=7
#nums=[3,4,5,6]

#brute force
def twosum(nums:list[int],target:int)->list[int]:
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
            
print(twosum(nums=[3,4,5,6,],target=7))            
#Time-O(n^2)
#space-O(1)
#works but too slow for large inputs


#HASH MAP(OPTIMAL SOLN)
def two_sum(nums,target):
    seen={} #value->index

    for i,num in enumerate(nums):
        complement=target-num #what number do we need?

        if complement in seen:
            return[seen[complement],i]
        
        seen[num]=i
        

    return []    


print(two_sum([3,4,5,6],7))