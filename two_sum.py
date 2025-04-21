from typing import List  # <-- Fix typo here

nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []  # In case no solution is found

# Create an instance and call the method
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]
