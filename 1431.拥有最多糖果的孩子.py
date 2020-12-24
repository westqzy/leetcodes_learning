#
# @lc app=leetcode.cn id=1431 lang=python3
#
# [1431] 拥有最多糖果的孩子
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        res = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candie:
                res[i] = True
        return res
# @lc code=end

