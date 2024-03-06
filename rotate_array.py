"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

def rotate_array(nums, k):
    # Handling the case where k is greater than the length of the array
    k = k % len(nums)
    
    # First, reverse the entire array
    nums.reverse()
    
    # Second, reverse the first k elements
    nums[:k] = reversed(nums[:k])
    
     # Last, reverse the remaining starting from k
    nums[k:] = reversed(nums[k:])
    
# Test case 1    
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate_array(nums1, k1)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

# Test case 2
nums2 = [-1, -100, 3, 99]
k2 = 2
rotate_array(nums2, k2)
print(nums2)  # Output: [3, 99, -1, -100]