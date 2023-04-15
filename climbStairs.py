class Solution:
    def climbStairs(self, n: int) -> int:
        n1=0
        n2=1
        for i in range(1,n+1):
            n3=n1+n2
            n1=n2
            n2=n3
        return n3


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))