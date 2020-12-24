#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#

# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # res = 0
        # for i in range(len(startTime)):
        #     if queryTime >= startTime[i] and queryTime <= endTime[i]:
        #         res += 1
        # return res
        return sum(i <= queryTime <=j for i,j in zip(startTime, endTime))
# @lc code=end

