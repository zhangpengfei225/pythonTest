
def checkPossibility(nums): 
        #[4,2,3]
        #[-1,4,2,3]
        #2,3,3,2,4

        #3,4,2,3
        flag = 0
        if len(nums)<=1 and len(nums)>=0:
            return True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                flag = i
                break
        if flag == len(nums)-1:
            return True

        newnums1 = nums[0:flag] + nums[flag+1:]
        newmums2 = nums[0:flag-1] + nums[flag:]
        return sorted(newnums1) == newnums1 or sorted(newmums2)==newmums2
checkPossibility([3,4,2,3])       