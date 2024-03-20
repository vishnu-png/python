def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0

    if nums[0] == 0:
        return -1

    jumps = 1
    max_reachable = nums[0]
    steps_possible = nums[0]

    for i in range(1, n):
        if i == n - 1:
            return jumps

        max_reachable = max(max_reachable, i + nums[i])
        steps_possible -= 1

        if steps_possible == 0:
            jumps += 1

            if i >= max_reachable:
                return -1

            steps_possible = max_reachable - i

    return -1
nums = [2, 3, 1, 1, 4]
print(min_jumps(nums))  
