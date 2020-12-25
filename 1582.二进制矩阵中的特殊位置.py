#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if  mat[i][j] == 1:
                    if sum(mat[i]) == 1 and sum(mat[k][j] for k in range(len(mat))) == 1:
                        res += 1
        return res
# @lc code=end

