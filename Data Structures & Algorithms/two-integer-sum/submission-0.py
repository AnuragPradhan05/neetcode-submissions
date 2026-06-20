class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        n = len(nums)

        for i in range(n):
            rest = target - nums[i]
            if rest not in table:
                table[nums[i]] = i
            else:
                return [table[rest],i]
