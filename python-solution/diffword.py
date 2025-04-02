def alg(strs):
    hashT = dict()
    for i in strs:
        s = "".join(sorted(i))
        if s not in hashT:
            hashT[s] = []
        hashT[s].append(i)
        
    return list(hashT.values())

def test():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(alg(strs))
    

test()