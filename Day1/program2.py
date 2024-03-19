def sumsquare(l):
    odd_sum = 0
    even_sum = 0

    for num in l:
        if num % 2 == 0:  # check if number is even
            even_sum += num ** 2
        else:
            odd_sum += num ** 2

    return [odd_sum, even_sum]

l = [1, 2, 3, 4, 5]
result = sumsquare(l)
print(result)  
