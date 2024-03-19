def is_match(s, p):
    if not p:  
        return not s 

    first_match = bool(s) and (p[0] == s[0] or p[0] == '.')  

    if len(p) >= 2 and p[1] == '*':  
        return (is_match(s, p[2:]) or  
                (first_match and is_match(s[1:], p)))  
    else:
        return first_match and is_match(s[1:], p[1:])  


s = "aa"
p = "a*"
print(is_match(s, p)) 
s = "mississippi"
p = "mis*is*p*."
print(is_match(s, p))  
