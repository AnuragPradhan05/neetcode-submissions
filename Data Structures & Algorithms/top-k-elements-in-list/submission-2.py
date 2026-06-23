class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        new = sorted(freq.items(),key = lambda x: x[1],reverse=True)

        for key,value in new:
            if k > 0:
                res.append(key)
                k -= 1

        return res
