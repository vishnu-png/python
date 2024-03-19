def isomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping = {}
    mapped_chars = set()

    for char_s, char_t in zip(s, t):
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        else:
            if char_t in mapped_chars:
                return False
            mapping[char_s] = char_t
            mapped_chars.add(char_t)

    return True

s1 = "egg"
t1 = "add"
print(isomorphic(s1, t1))  

s2 = "foo"
t2 = "bar"
print(isomorphic(s2, t2))  
