def longestPalindromicSubstring(string):
    # Write your code here.
	start,end =0,0
    for i in range(len(string)):
		oddLen = getPalindromeLength(string,i,i)
		evenLen = getPalindromeLength(string,i,i+1)
		
		size = max(oddLen,evenLen)
		
		if size > end - start:
			start = i - (size-1)//2
			end = i + size//2
	return string[start:end+1]
	
def getPalindromeLength(string,l,h):
	while l>=0 and h<len(string) and string[l] == string[h]:
		l-=1
		h+=1
	return h-l-1