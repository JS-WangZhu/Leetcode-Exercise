class Solution:
    def convert(self, s: str, numRows: int) -> str:
        reslist = [[] for i in range(numRows)]
        #求循环子串
        num = numRows
        ll = []
        for i in range(num):
            ll.append(i+1)
        truthlooplength = num*2 - 2
        for i in range(truthlooplength - num):
            ll.append(ll[num-i-2])
        loopsize = len(ll)
        #padding
        strlen = len(s)
        strfinalindexlist = []
        for charindex in range(strlen):
            strfinalindexlist.append(ll[charindex%loopsize])
        for charindex in range(strlen):
            reslist[strfinalindexlist[charindex]-1].append(s[charindex])
        fstr = ''
        for i in reslist:
            tmp = ''
            for j in i:
                tmp += j
            fstr+=str(tmp)
        return fstr