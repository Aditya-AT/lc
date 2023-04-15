from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sets = set(nums)
        res = []
        for i in range(len(nums)):
            if i+1 not in sets:
                res.append(i+1)
        return res

if __name__ == '__main__':
    f = Solution()
    print(f.findDisappearedNumbers([1,2,6,5,9]))
