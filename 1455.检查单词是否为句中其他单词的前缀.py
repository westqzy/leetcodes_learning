#
# @lc app=leetcode.cn id=1455 lang=python3
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            if sentence[i][:len(searchWord)] == searchWord:
                return i+1
        return -1
# @lc code=end

