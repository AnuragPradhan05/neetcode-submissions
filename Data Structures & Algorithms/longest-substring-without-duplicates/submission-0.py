class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0

        LSS = set()
        maxLen = 0

        for j in range(len(s)):
            while s[j] in LSS:
                LSS.remove(s[i])
                i += 1

            LSS.add(s[j])
            maxLen = max(maxLen,j - i + 1)

        return maxLen
            

