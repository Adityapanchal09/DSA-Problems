s = "XYYYX"
k=2
s1 = "AAABABB"
k1=1

s2="AABABBA"
k2=1

def long_substring(s,k):
    count = {}
    r=0
    l=0
    max_freq=0
    result=0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq=max(count[s[r]],max_freq)

        window_size=r-l+1
        if window_size-max_freq > k:
            count[s[l]]-=1
            l+=1
        result=max(result,r-l+1)
    return result    

print(long_substring(s,k))
print(long_substring(s1,k1))
print(long_substring(s2,k2))