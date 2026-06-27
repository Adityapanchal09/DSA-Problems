'''Given the array of strings "strs" group the anagrams together into sublists.
You may return the output in any order'''

strs=["act","pots","tops","cat","stop","hat"]

#Output:[["hat"],["act","cat"],["stop","pots","tops"]]

from collections import defaultdict

def groupanagrams(strs):
    groups=defaultdict(list)        #auto creates empty empty list for any new key

    for word in strs:
        key=tuple(sorted(word))    #returns immutable tuple key valid for dict
                                    #key=('a','e','t')
        
        groups[key].append(word)    #groups[('a','e','t')].append("eat")-->[('a','e','t'):["eat"]]

    return list(groups.values())    #will return [["eat","ate"],["cat","tac"]]


print(groupanagrams(strs))