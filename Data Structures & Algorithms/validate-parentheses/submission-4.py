class Solution:
    def isValid(self, s: str) -> bool:
        
        target = {"}":"{", "]":"[", ")": "("}
        stack =[]

        for i in range(len(s)):
            if stack and s[i] in target and stack[-1]==target[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return len(stack)==0
