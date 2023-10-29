# Question

# Write a function to crush candy in one dimensional board. In candy crushing games,
# groups of like items are removed from the board. In this problem, any sequence of 3 or more like items should be removed 
# and any items adjacent to that sequence should now be considered adjacent to each other. This process should be repeated
# as many time as possible. You should greedily remove characters from left to right.


# input
# Input: "aabbccddeeedcba"
# Output: ""
# Explanation:
# 1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
# 2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
# 3. Remove 3 'c': "aabbcccba" => "aabbba"
# 4. Remove 3 'b': "aabbba" => "aaa"
# 5. Remove 3 'a': "aaa" => ""


# def candy_crush(input):
#     if not input:
#         return input
    
#     stack = []
#     stack.append([input[0], 1])
    
#     for i in range(1, len(input)):
#         if input[i] != input[i-1]:
#             if stack[-1][1] >= 3:
#                 stack.pop()
#             if stack and stack[-1][0] == input[i]:
#                 stack[-1][1] += 1
#             else:
#                 stack.append([input[i], 1])
#         else:
#             stack[-1][1] += 1
            
#     # handle end
#     if stack[-1][1] >= 3:
#         stack.pop()
        
#     out = []
#     for ltrs in stack:
#         out += ltrs[0] * ltrs[1]
    
#     return ''.join(out)


# print(candy_crush("aabbccddeeedcbak"))


def cc(input):
    if not input:
        return input

    stack = []
    stack.append([input[0], 1])

    for i in range(1, len(input)):
        if input[i] != input[i-1]:
            if stack[-1][1] >= 3:
                stack.pop()
            if stack and stack[-1][0] == input[i]:
                stack[-1][1] += 1
            else:
                stack.append([input[i], 1])
        if input[i] == input[i-1]:
            stack[-1][1] += 1

    
    if stack[-1][1] >= 3:
        stack.pop()

    out = []
    for lt in stack:
        out += lt[0] *lt[1]
    
    return ''.join(out)

print(cc("aabbccddeeedcba"))