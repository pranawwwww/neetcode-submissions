class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
  
        for word in strs:
            c = [0]*26
            for x in word:
                c[ord(x) - ord('a')]+=1
            anagrams[tuple(c)].append(word)

        return list(anagrams.values())
        