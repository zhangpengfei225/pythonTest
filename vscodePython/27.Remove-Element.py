def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    j = 0
    print(nums)
    while j<len(nums):
        if nums[j] == val:
            count+=1
        else:
            nums[j-count] = nums[j]    
        j+=1
    print(nums[0:len(nums)-count+1])
    print(nums)
    return len(nums)-count+1

print(removeElement([0,1,2,2,3,0,4,2],2))



      
               
       