def plusOne(digits):
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

print(plusOne([1,2,3]))