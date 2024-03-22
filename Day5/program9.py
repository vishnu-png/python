def shuffle(l1, l2):
    shuffled = []
    min_len = min(len(l1), len(l2))
    
    for i in range(min_len):
        shuffled.append(l1[i])
        shuffled.append(l2[i])
    if len(l1) > min_len:
        shuffled.extend(l1[min_len:])
    elif len(l2) > min_len:
        shuffled.extend(l2[min_len:])
    
    return shuffled

l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c']
print(shuffle(l1, l2))  
