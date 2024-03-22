def longestSubstring(s, k):
    if len(s) == 0 or k > len(s):
        return 0
    
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1

    for char, count in counter.items():
        if count < k:
            return max(longestSubstring(substring, k) for substring in s.split(char))
    
    return len(s)

s = "aaabb"
k = 3
print(longestSubstring(s, k))  
