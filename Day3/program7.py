from itertools import permutations

def permute_unique(nums):
    unique_nums = set(nums)
    result = []
    for perm in permutations(unique_nums):
        result.append(list(perm))
    return result
nums = [1, 2, 2]
print(permute_unique(nums))
