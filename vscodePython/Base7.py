def convertToBase7(num):
    #注意特殊情况num==0
    if num==0:
        return "0"
    lis = []
    temp = num
    if num<0:
        num=-num
    while num:
        lis.append(num%7)
        num = num//7
    result = "".join([str(lis[i]) for i in range(len(lis)-1,-1,-1)])
    if temp<0:
        return "-"+ result
    return result
print(convertToBase7(-7))