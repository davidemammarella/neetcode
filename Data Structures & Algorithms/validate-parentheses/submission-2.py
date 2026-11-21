class Solution:
    def isValid(self, s: str) -> bool:

        lifo = []
        par = {"}":"{", "]":"[", ")":"("}

        for i in range(len(s)):

            if lifo and lifo[-1]==par.get(s[i]):
                lifo.pop()
            else:
                lifo.append(s[i])
        
        return len(lifo)==0