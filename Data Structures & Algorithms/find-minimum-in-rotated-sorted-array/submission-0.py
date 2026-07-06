class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = nums[0]
        last = nums[-1]

        low = 0
        high = len(nums)-1
        if first <= last:
            return first

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > last:
                low = mid + 1

            else:
                high = mid
            

        return nums[low]