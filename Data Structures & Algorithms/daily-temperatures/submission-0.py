class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            if stack == []:
                stack.append(i)
            else:
                while stack  and temperatures[i] > temperatures[stack[-1]]:
                    popedIndex = stack.pop()
                    resIndex = i - popedIndex
                    res[popedIndex] = resIndex
                stack.append(i)
        return res


