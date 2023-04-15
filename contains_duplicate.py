class Solution:
    def containsDuplicate(nums) -> bool:
        #O(n^2)
        for i in range(len(nums)):
            count = 0
            print(count, 'init')
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    print(count, 'end')
                    if count >= 2:
                        return 'true'
        return 'false'

        def containsDuplicate_2(nums) -> bool:
            # O(n) create set
            return len(set(nums)) != len(nums)


if __name__ == '__main__':
    print(Solution.containsDuplicate([1,2,3,4]))