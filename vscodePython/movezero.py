def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        numzero=0
        for item in nums:
            if item ==0:
                numzero+=1
        count = 0
        i = 0
        length=len(nums)
        if length!=numzero and numzero>0:
            while(i<length):
                
                if nums[i] == 0:
                    count+=1
                    if i+1<length:
                        if nums[i+1]!=0:
                            nums[i+1-count] = nums[i+1]
                            i+=2
                        else:
                            count+=1
                            i+=2
                else:
                    nums[i-count] = nums[i]
                    i+=1
                
            for i in range(length-count,length):
                nums[i]=0
        print(nums)

moveZeroes([0,1,0,3,12])