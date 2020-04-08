#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (34.82%)
# Total Accepted:    329K
# Total Submissions: 944.8K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
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



        

        

