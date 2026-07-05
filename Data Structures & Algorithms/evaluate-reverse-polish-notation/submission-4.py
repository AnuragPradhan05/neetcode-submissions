class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp_List = ["+","-","*","/"]
        res = []
        exp = ""
        for ex in tokens:
            if ex in exp_List and ex == "+":
                result = int(res.pop()) + int(res.pop())
                res.append(result)

            elif ex in exp_List and ex == "*":
                result = int(res.pop()) * int(res.pop())
                res.append(result)

            elif ex in exp_List and ex == "/":
                a = res.pop()
                b = res.pop()
                result = int(int(b) / int(a))
                res.append(result)

            elif ex in exp_List and ex == "-":
                a = res.pop()
                b = res.pop()
                result = int(b) - int(a)
                res.append(result)

            else:
                res.append(ex)

        return int(res[-1])

