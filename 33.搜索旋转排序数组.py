    #
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # copy_num_pos = dict(zip(nums, range(len(nums))))
        # print(copy_num_pos)
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         nums = nums[i:] + nums[:i]
        #         break
        # left = 0
        # right = len(nums)-1
        # while left <= right:
        #     mid = (left + right)//2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         return copy_num_pos[nums[mid]]
        # return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right + left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:# 表明左侧有序
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:# 表明you侧有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            #print(left, mid, right)
        return -1
        # try:
        #     return nums.index(target)
        # except:
        #     return -1
# @lc code=end
nums= [4,5,6,7,0,1,2]
s = "-".join(map(str, nums))

print(s)