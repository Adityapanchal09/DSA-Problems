#Here an optimal solution would be of time complexity of O(n)
nums=[1,2,3,1]

def check_duplicate_brute(nums):      #time complexity-O(n^2)(two loops 1 inside another,checks every pair)
                                        # space Complexity-O(1)(no extra memory used)
                                        #not an optimal solution
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True       
    return False    


print(check_duplicate_brute(nums))


def hash_check_duplicate(nums):
    seen=set()      #empty set to track numbers we have seen
    for num in nums:
        if num in seen:     #already seen this number? duplicate!
            return True
        seen.add(num)       #havent seen it yet add to set

    return False        #went through all numbers no duplicate  

print(hash_check_duplicate(nums))


#time :O(n)-one pass through the array
#space :O(n)-set grows up to n elements

#it is an optimal solution



#one liner bonus
def has_duplicate(nums):
    return len(nums)!=len(set(nums))

print(has_duplicate(nums))