#to return true if two variables comapred contains same type of letters with same amount

s="anagram"
t="nagaram"

#Approach1----
#sort both the strings
def is_anagram(s,t):                                 #time-O(n log n)sorting takes n logn
    return sorted(s)==sorted(t)                      #space:o(n)
                                                    #simple but not optimal ,sorting is wasteful
print(is_anagram(s,t))                                                    #for this problem



#Approach2----
def isAnagram(s,t):
    #if different lengths--cant be anagram
    if len(s)!=len(t):
        return False
    
    count={} #char->frequncy

    for char in s:
        count[char]=count.get(char,0)+1 #count char in s
    for char in t:
        count[char]=count.get(char,0)-1 #subtract char in t if same as s
        if count[char]<0:
            return False #t has more of this char than s

    return True        


print(isAnagram(s,t)) #time--O(n)-two passes through strings
                #space---O(1)-at most 26 characters(lowercase letters)


#python one liner--
from collections import Counter

def check_anagram(s,t):
    return Counter(s)==Counter(t)

print(check_anagram(s,t))

#Counter("anagram")->{'a':3,'n':1,'g':1,'r':1,'m':1}
#comparing two counters check if all character frequencies match 