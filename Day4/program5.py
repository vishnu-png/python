def minJumps(nums):
    if not nums or nums[0] == 0:
        return -1

    n = len(nums)
    jumps = 0
    max_reach = nums[0]
    steps = nums[0]

    for i in range(1, n):
        if i == n - 1:
            return jumps + 1

        max_reach = max(max_reach, i + nums[i])
        steps -= 1

        if steps == 0:
            jumps += 1

            if i >= max_reach:
                return -1

            steps = max_reach - i

    return jumps

nums = [2, 3, 1, 1, 4]
print(minJumps(nums))  # Output: 2
