class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            countT[c]+=1
        have = 0
        need = len(countT)
        reslen = len(s)+1
        res = [-1,-1]
        l=0
        for r in range(len(s)):
            window[s[r]]+=1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have+=1
            while have == need:
                if (r-l+1)<reslen:
                    res  = [l,r]
                    reslen = r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                
                l+=1
        if reslen == len(s)+1:
            return ""
        l,r = res
        return s[l:r+1]
            


        