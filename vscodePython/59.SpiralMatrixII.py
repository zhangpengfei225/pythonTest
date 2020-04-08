class Solution:
    def generateMatrix(self, n: int):
        res = [[0 for i in range(n)] for i in range(n)]
    # 主要是按圈打印,分为奇数和偶数单独考虑
    #设置打印次数为count
        if n % 2 == 0:
            count = n//2
        else:
            count = n//2+1
        num = 1
        for i in range(count):
            # 打印上面一行
            for k1 in range(i, n-i):
                res[i][k1] = num
                num+=1
            # 打印右边一列
            for k2 in range(i+1, n-i):
                res[k2][n-1-i] = num
                num+=1
            # 打印下面一行
            for k3 in range(n-i-1-1,i-1,-1):
                res[n-1-i][k3] = num
                num+=1
            for k4 in range(n-i-1-1,i,-1):
                res[k4][i] = num
                num+=1
        return res
