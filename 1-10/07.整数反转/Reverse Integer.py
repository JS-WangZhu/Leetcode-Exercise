class Solution:
    def reverse(self, x: int) -> int:
        num = x
        finalnum = 0
        if num<0:
            num = -num
            numlist = []
            for i in str(num):
                numlist.insert(0,i)
            numstr = ''.join(numlist)
            finalnum = -int(numstr)
        else:
            numlist = []
            for i in str(num):
                numlist.insert(0,i)
            numstr = ''.join(numlist)
            finalnum = int(numstr)
        #判断是否符合范围
        try:
            assert -2**31 <= finalnum <= 2**31 -1
        except:
            finalnum = 0
        return finalnum
