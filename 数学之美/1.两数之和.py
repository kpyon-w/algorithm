#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        n = len(nums)
        map = {}
        
        for i in range(n):
            if((target - nums[i]) in map):
                return [map[target - nums[i]], i]
            else:
                map[nums[i]] = i
        return []

# @lc code=end