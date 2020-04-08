def findLengthOfLCIS(nums: List[int]) -> int:
        #using dp
        
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        lis=[1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                lis[i] = lis[i-1] + 1   
        return max(lis)