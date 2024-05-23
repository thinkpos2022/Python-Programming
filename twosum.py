def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            #print("Found:", num, "at index", i)
            print("Found complement:", complement, "at index", num_indices[complement])
            return [num_indices[complement], i]
        num_indices[num] = i
        print("Current num:", num, "at index", i)
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
