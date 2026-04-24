class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in map:
                return map[difference], index
            map[value] = index