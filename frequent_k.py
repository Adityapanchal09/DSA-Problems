#Hash MAP +sorting
nums=[1,2,2,3,3,3,4,4]
k=2
#output=[2,3]

def frequent_k(nums,k):
    count={}

    for num in nums:
        count[num]=count.get(num,0)+1 

    return sorted(count,key=lambda x:count[x],reverse=True)[:k]
    

print(frequent_k(nums,k))

#here problems:1)will only return upto k values if [4:2,2:2,3:3,1:1] should return [4,3,2] 
#but returns only [3,2]

#2)time-O(n logn)-sorting  # not an optimal approach


#optimal Approach (Bucket Sort):
def frequent_k_value(nums,k):
    count={}

    for num in nums:
        count[num]=count.get(num,0)+1
        
        
    freq=[[] for _ in range(len(nums)+1)]
    for num,cnt in count.items():
        freq[cnt].append(num)


    result=[]
    for i in range(len(freq)-1,0,-1):
        for num in freq[i]:
            result.append(num)
            if len(result)==k:
                return result        
    return result            

print(frequent_k_value(nums,k))

