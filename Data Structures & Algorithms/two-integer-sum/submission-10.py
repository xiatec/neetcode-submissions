class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            cur = target - n
            if cur in indices:
                return [indices[cur], i]
            indices[n] = i
