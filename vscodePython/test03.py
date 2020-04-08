def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        new = nums1[0:m]
        i = 0
        j = 0
        count = 0
        while(i<=m and j<=n):
            if new[i]<nums2[j]:
                nums1[count] = new[i]
                i+=1
            else:
                nums1[count] = nums2[j]
                j+=1
            count+=1
        if  i>m and j<n:
            nums1 = nums2[j:n]
        if  j>n and i<m:
            nums1 = new[i:m]
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
merge(nums1, m, nums2, n)
print(nums1)
#nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
#新建了一个文件
def modfunc():
    return