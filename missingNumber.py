from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([1,6,4,8]))