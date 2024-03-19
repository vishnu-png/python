def is_happy(n):
    def square_sum(num):
        sum_of_squares = 0
        while num > 0:
            digit = num % 10
            sum_of_squares += digit ** 2
            num //= 10
        return sum_of_squares

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = square_sum(n)

    return n == 1
print(is_happy(19))  
print(is_happy(4))  
