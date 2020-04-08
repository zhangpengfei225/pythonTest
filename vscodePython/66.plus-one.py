#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (40.66%)
# Total Accepted:    352.9K
# Total Submissions: 867.9K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
# 
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [0]:
            return [1]
        if (digits[-1]+1)<10:
            digits[-1]+=1
            return digits
        if (digits[-1]+1)>=10:
            temp = 0
            digits[-1]=(digits[-1]+1+temp)%10
            temp = 1
            for i in range(len(digits)-2,-1,-1):
                extra = digits[i]
                digits[i]=(digits[i]+temp)%10
                temp = (extra+temp)//10
                
        if temp:
            return [1]+digits
        else:
            return digits



        

