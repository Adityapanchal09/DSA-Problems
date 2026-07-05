nums=[-1,0,1,2,-1,-4]

def three_sum(nums):
    result=[]
    nums.sort()
    #[-4,-1-1,0,1,2]

    for i in range(len(nums)):
        l=i+1
        r=len(nums)-1
        if i!=0 and nums[i]==nums[i-1]:     #skip duplicates 
            continue
        while l<r:
            total=nums[i]+nums[l]+nums[r]
            if total>0:
                r-=1
            elif total<0:
                l+=1
            else:
                result.append([nums[i],nums[l],nums[r]])
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1            

    return result   

print(three_sum(nums))         