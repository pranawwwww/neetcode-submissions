class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        sl1 = [0]*26
        sl2 = [0]*26
        for i in range(len(s1)):
            sl1[ord(s1[i])-ord('a')]+=1
            sl2[ord(s2[i])-ord('a')]+=1
        if sl1 == sl2:
            return True
        l=0

        for r in range(len(s1),len(s2)):
            
            sl2[ord(s2[l]) - ord('a')] -= 1
            sl2[ord(s2[r]) - ord('a')] += 1
            l+=1
            if sl1 == sl2:
                return True
        return False
