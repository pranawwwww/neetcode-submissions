class Solution:
    def isValid(self, s: str) -> bool:
        valids={']':'[',"}":"{",")":"("}
        stack=[]
        for i in s:
            if i in list(valids.values()):
                stack.append(i)
            else:
                if stack and stack[-1] == valids[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

        