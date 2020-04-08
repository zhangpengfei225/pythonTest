#def findJudge(self, N: int, trust: List[List[int]]) 
#19/2/25/9:56
def findJudge(n, trustlist):
    judgeSet = set()
    judgeKey = set()
    #挑选出所有的候选judge
    for i in range(len(trustlist)):
        judgeSet.add(trustlist[i][1])
        judgeKey.add(trustlist[i][0])
    

    judgeSet2 = set()
    for judgeItem in judgeSet:
        if judgeItem is not in judgeKey:
            for listItem in trustlist:
                if listItem[1]==judgeItem :
                    judgeSet2.add(listItem[0])
            if (len(judgeSet2)!=n-1):
                judgeSet.remove(judgeItem)
        else:
            judgeSet.remove(judgeItem)
        
    if len(judgeSet)!=1:
        return -1
    else:
        return judgeSet[0]
    
print(findJudge(2,[[1,2]]))