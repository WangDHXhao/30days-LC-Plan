
"""
两数之和
核心思想
哈希表
"""


from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]]=i
            else:
                return [i,dict[target-nums[i]]]



if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9
    s=Solution()

    print(s.twoSum(nums, target))
