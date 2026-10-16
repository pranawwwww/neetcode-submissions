class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for word in strs:
            x = "".join(sorted(word))
            if x in anagrams.keys():
                anagrams[x].append(word)
            else:
                anagrams[x] = [word]
        return list(anagrams.values())
        