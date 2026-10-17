class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        suffix = [1]*len(nums)
        for i in range(1,len(nums)):
            pref[i] = nums[i-1]*pref[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = nums[j+1]*suffix[j+1]
        res=[]
        for k in range(len(nums)):
            res.append(pref[k]*suffix[k])
        return res


            
        