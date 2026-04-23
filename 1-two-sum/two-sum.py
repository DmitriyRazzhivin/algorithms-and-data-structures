class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}
        for i, n in enumerate(nums):
            y = target - n
            if y in map:
                return [map[y], i]
            map[n] = i
