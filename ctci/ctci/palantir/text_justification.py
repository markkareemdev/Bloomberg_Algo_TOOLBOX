def split_s(s):
    res = []
    for word in s:
        res += word.split()
    return res

def fullJustify(words,maxWidth):
        ans, cur = [], []
        chars = 0
        words = split_s(words)
        for word in words:
            # if cur is empty or the total chars + total needed spaces + next word fit
            if not cur or (len(word) + chars + len(cur)) <= maxWidth:
                cur.append(word)
                chars += len(word)
            else:
                # place spaces, append the line to the ans, and move on
                
                line = placeSpacesBetween(cur, maxWidth - chars)
                ans.append(line)
                cur.clear()
                cur.append(word)
                chars = len(word)
                    
                    
        if len(cur) == 1:
            return ans + cur
        else:
            return ans + [placeSpacesBetween(cur,maxWidth - chars)]
        
    
def placeSpacesBetween(words, spaces):
    if len(words) == 1: return words[0]
    
    space_groups = len(words)-1
    spaces_between_words = spaces // space_groups
    extra_spaces = spaces % space_groups
    
    cur = []
    for word in words:
        cur.append(word)
        
        # place the min of remaining spaces or spaces between words plus an extra if available
        cur_extra = min(1, extra_spaces)
        spaces_to_place = min(spaces_between_words + cur_extra, spaces)

        cur.append(' ' * spaces_to_place)
        
        if extra_spaces: extra_spaces -= 1
        spaces -= spaces_to_place
    
    return ''.join(cur)

print(fullJustify(["Some modern typesetting programs","offer four justification","options"],24))
print(fullJustify(["The Earth is","the only world","known so far","to harbor life"],18))
print(fullJustify(["It underscores our responsibility","to deal more kindly with one another"],15))

