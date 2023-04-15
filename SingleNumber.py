from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if len(nums) != 1:
                if i == 0:
                    if nums[i] != nums[i+1]:
                        return nums[i]
                elif i == len(nums)-1:
                    if nums[i] != nums[i-1]:
                        return nums[i]
                else:
                    if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                        return nums[i]
            else:
                return nums[0]
