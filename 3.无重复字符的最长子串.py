#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash1 = dict()
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] in hash1.keys() and hash1[s[i]]>=start:
                start = hash1[s[i]]+1
            hash1[s[i]] = i
            print(start, i)
            res = max(res, i - start + 1)
            
        return res
# @lc code=end

