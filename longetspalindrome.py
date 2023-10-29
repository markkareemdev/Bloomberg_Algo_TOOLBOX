"""
Given a string s, return the longest palindromic substring in s
"""

def lpalindrome(s):

    # find the length of the string
    n = len(s)

    # create a list to store al the palindromes
    dromes = []

    # initialize the index with the longest pali substring and max length
    maxlen = 0
    maxindex = 0

    # loop through the items in the string
    for i in range(n):
        
        # get the index of the next character
        nxt = i+1

        while nxt <= n-1:
            # create a new string with the index
            ns = s[i:nxt+1]
            # print(ns[ : : -1])
            

            # check if palindrome
            if ns == ns[ : : -1]:
                dromes.append(ns)

                # find the length of the new found palindrome
                palilen = len(ns)

                # check max index
                if palilen > maxlen:
                    maxlen = palilen
                    maxindex = len(dromes) - 1
                
                # increase the count
                nxt += 1
            else:
                nxt += 1

    if not dromes:
        return None
    return dromes[maxindex]
        

            

ss = 'mjjm'
print(lpalindrome(ss))
