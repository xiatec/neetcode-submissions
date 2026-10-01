class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = []
        for i, n in enumerate(nums):
            nums_copy.append([i, n])
        nums_copy.sort(key=lambda x:x[1])

        i, j = 0, len(nums)-1
        while i < j:
            cur = nums_copy[i][1] + nums_copy[j][1]
            if cur == target:
                return[min(nums_copy[i][0],nums_copy[j][0]),max(nums_copy[i][0],nums_copy[j][0])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
        