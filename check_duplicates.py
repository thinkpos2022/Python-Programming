"""Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Test case 1:
Input: nums = [1,2,3,1]
Output: true

Test case 2:
Input: nums = [1,2,3,4]
Output: false

Test case 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class ContainsDuplicate:
    def check_duplicate(self, nums):
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
        return False
       
nums1 = [1, 2, 3, 1]
dupl_nums = ContainsDuplicate()
output1 = dupl_nums.check_duplicate(nums1)
print(output1)

nums2 = [1, 2, 3, 4]
dupl_nums = ContainsDuplicate()
output2 = dupl_nums.check_duplicate(nums2)
print(output2)

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
dupl_nums = ContainsDuplicate()
output3 = dupl_nums.check_duplicate(nums3)
print(output3)
