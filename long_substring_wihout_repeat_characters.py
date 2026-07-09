s="zxyzxyz"
#output=3

def long_substring(s):
    left=0
    seen=set()
    result=0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right]) 
        result=max(result,right-left+1)
    return result


print(long_substring(s))

#time=o(n) each character is added and removed at once
#space=O(k) where k is the size of character set