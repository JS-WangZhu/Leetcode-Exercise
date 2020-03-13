class Solution:
    def romanToInt(self, s: str) -> int:
        final_num = 0
        special_num = {'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
        normal_num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for item in special_num:
            res = s.find(item)
            if res >=0:
                s = s[0:res]+s[res+2:]
                final_num += special_num[item]
        for i in s:
            final_num += normal_num[i]
        return final_num