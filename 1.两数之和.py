#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):  # x=nums[i]
            for j in range(i + 1, len(nums)):  # 枚举 i 右边的 j
                if x + nums[j] == target:  # 满足要求
                    return [i, j]  # 返回两个数的下标
        # 这里无需 return，因为题目保证有解
        
# @lc code=end

