class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=[0]*3000
        for i in nums:
            x[i+1000]+=1
        res = []
        for j in range(k):
            m = max(x)
            res.append(x.index(m)-1000)
            x[x.index(m)] = 0

        return res
        