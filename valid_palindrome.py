s="wasitacaroracatisaw"

#valid palindrome=returns true if dtring reads forward and backword same

def validpalindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        #skip alphanumeric characters from left
        while left<right and not s[left].isalnum():
            left+=1

        #skip alphanumeric characters from right
        while left<right and not s[right].isalnum():
            right-=1

        #compare charcters(case sensetive)
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True
        

print(validpalindrome(s))        


#python oneliner
def validPalindrome(s):
    clean=[c.lower()for c in s while  not c.isalnum()]
    return clean==clean[::-1]

print(validPalindrome(s))