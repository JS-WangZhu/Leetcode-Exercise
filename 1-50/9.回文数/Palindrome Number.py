class Solution:
    def isPalindrome(self, x: int) -> bool:
        finalresstr = ''
        if x<0:
            return False
        else:
            tmplist = []
            for i in str(x):
                tmplist.insert(0,i)
            finalresstr = ''.join(tmplist)
        if finalresstr == str(x):
            return True
        else:
            return False
