from typing import List

#https://leetcode.com/problems/counting-bits/solutions/79557/how-we-handle-this-question-on-interview-thinking-process-dp-solution/
def countBits(n: int):
    res = []
    for i in range(n+1):
        res.append((bin(i)).count('1'))
    return res

print(countBits(12))