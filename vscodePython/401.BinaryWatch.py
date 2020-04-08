class Solution:
    def readBinaryWatch(self, n: int):
        if n == 0: return ["0:00"]
        def mysum(lis,n,res,temp,deep,flag):
            if deep == n:
                sums = sum(temp)
                if sums not in res:
                    res.append(sums)
            else:
                for i in range(deep, len(lis)):
                    if flag[i] == 0:
                        temp.append(lis[i])
                        flag[i] = 1
                        mysum(lis,n,res, temp, deep+1,flag)
                        flag[i] = 0
                        temp.pop()

        def help(lis, k):
            res = []
            temp = []
            flag = [0 for i in range(len(lis))]
            mysum(lis,k,res,temp,0,flag)
            # print(res)
            return res
        
        lis_minutes = [1,2,4,8,16,32]
        lis_hours = [1,2,4,8]
        hours = [ i for i in range(0, min(4,n)+1)]
        minutes = []
        for i in hours:
            minutes.append(n-i)
        for k in range(len(minutes)):
            if (minutes[k]<=6):
                minutes = minutes[k:]
                hours = hours[k:]
                break
        #print(minutes,hours)
        sum_minutes = []
        sum_hours = []
        for i in range(len(minutes)):
            sum_minutes.append(help(lis_minutes, minutes[i]))
            sum_hours.append(help(lis_hours, hours[i]))
        #print(sum_minutes,sum_hours)
        res = []
        for i in range(len(sum_hours)):
            res.append([sum_hours[i],sum_minutes[i]])

        last_ans = []
        for item in res:
            ans_hours = item[0]
            ans_minutes = item[1]
            for i in ans_hours:
                if i>11: continue
                for j in ans_minutes:
                    if j >59: continue
                    if j < 10: j = "0"+str(j)
                    if str(i)+":"+str(j)!="0:00":
                        last_ans.append(str(i)+":"+str(j))

        return last_ans
