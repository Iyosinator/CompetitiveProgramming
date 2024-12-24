def countSpecialSubstrings(s: str) -> int:
    n = len(s)
    left = 0
    result = 0
    char_set = set()
    
    for right in range(n):
        # If the character is already in the set, move the left pointer
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Add the count of special substrings ending at `right`
        result += (right - left + 1)
    
    return result
