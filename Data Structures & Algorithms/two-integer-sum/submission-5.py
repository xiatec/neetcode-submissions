class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i
        for i, n in enumerate(nums):
            cur = target - n
            if cur in indices and indices[cur] != i:
                return [i, indices[cur]]
        return 
        