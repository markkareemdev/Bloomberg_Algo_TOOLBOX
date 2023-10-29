def palindromePermutation(s):
    d = dict()
    for i in s.lower():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)
    found = False
    for k in d.keys():
        if k.isalpha(): #do not check for space
            if d[k]%2 == 1:
                if found:
                    return False
                found = True
    return True
print(palindromePermutation("Tact Coa"))