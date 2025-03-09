def find_two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        temp = target - num
        if temp in num_map:
            return [num_map[temp], i]
        num_map[num] = i
