strs=["hello","world"]
class solution:
    def encode(strs):
        encoded=""
        for s in strs:
            encoded+=f"{len(s)}#{s}"
        return encoded


    def decode(encoded):
        decoded=[]
        i=0
        while i<len(encoded):
            j=encoded.index("#",i) #find the # from position i
            length=int(encoded[i:j]) #everything between i and # is length
            word=encoded[j+1:j+1+length] #slice exactly 'length' chars from #
            decoded.append(word)
            i=j+1+length  #move i to start of next word
        return decoded


encoded_string=solution.encode(strs)
print(encoded_string)
print(solution.decode(encoded_string))