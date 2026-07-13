numbers=[100,4,200,1,2,3]
#output=4

def consecutive_sequence(numbers):
    seen=set(numbers)
    longest=0
     
    for num in seen:
        if num-1 not in seen:
            length=1
            while num + length in seen:
                length+=1
            longest=max(length,longest)
    return longest             


print(consecutive_sequence(numbers))

#time=O(n) here numbers are visited at most twice as for loop and inner while loop but
#numbers that arent sequence are skipped entirely so total work across all iterations is
# o(n)
#space=O(n)  the set conversion