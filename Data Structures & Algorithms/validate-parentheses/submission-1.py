class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictS = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in dictS.values():
                stack.append(i)

            else:
                if stack == []:
                    return False
                if stack[-1] == dictS[i]:
                    stack.pop()

                else:
                    return False

        if stack == []:
            return True
        else:
            return False
