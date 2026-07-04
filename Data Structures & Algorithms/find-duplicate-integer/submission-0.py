class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1

        for key,value in freq.items():
            if freq[key] > 1:
                return key

