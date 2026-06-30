nums=[1,2,4,6]
#output=[48,24,12,8]

def product_except_self(nums):
    n=len(nums)
    result=[1]*n

    prefix=1
    for i in range(n):
        result[i]=prefix
        prefix*=nums[i]

    suffix=1
    for i in range(n-1,-1,-1):
        result[i]*=suffix
        suffix*=nums[i]    

    return result


print(product_except_self(nums))
