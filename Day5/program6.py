def generate_triangle(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    
    for i in range(n):
        triangle[i][0] = 1
        triangle[i][i] = 1
    
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    return triangle

def sum_of_nth_row(triangle, n):
    if n <= 0:
        return 0
    
    return sum(triangle[n - 1])

n = 5
triangle = generate_triangle(n)
print("Triangular array:")
for row in triangle:
    print(row)
print("Sum of elements in the", n, "th row:", sum_of_nth_row(triangle, n))
