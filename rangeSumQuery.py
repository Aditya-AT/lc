from itertools import accumulate
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=[0]+list(accumulate(nums))
        print(self.nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1]-self.nums[left]

if __name__ == '__main__':
    N = NumArray()
    print(N.nums([[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]))
