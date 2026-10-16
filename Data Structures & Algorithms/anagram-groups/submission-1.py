class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        for word in strs:
            x = "".join(sorted(word))
            anagrams[x].append(word)
        return list(anagrams.values())
        