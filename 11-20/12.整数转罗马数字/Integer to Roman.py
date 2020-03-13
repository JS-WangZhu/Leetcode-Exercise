class Solution:
    def intToRoman(self, num: int) -> str:
        resstr = ''
        lessnum = num
        # 大于1000
        if num>=1000:
            thousand = int(num/1000)
            lessnum = num - thousand*1000
            resstr += 'M'*thousand

        # 大于500
        if lessnum>=500:
            if lessnum>=900:
                lessnum = lessnum - 900
                resstr += 'CM'
            else:
                lessnum = lessnum - 500
                resstr += 'D'

        # 大于100
        if lessnum>=100:
            if lessnum>=400:
                lessnum = lessnum - 400
                resstr += 'CD'
            else:
                onehundred = int(lessnum/100)
                lessnum = lessnum - onehundred*100
                resstr += 'C'*onehundred

        # 大于50
        if lessnum>=50:
            if lessnum>=90:
                lessnum = lessnum - 90
                resstr += 'XC'
            else:
                fifty = int(lessnum/50)
                lessnum = lessnum - fifty*50
                resstr += 'L'*fifty

        # 大于10
        if lessnum>=10:
            if lessnum>=40:
                lessnum = lessnum - 40
                resstr += 'XL'
            else:
                ten = int(lessnum/10)
                lessnum = lessnum - ten*10
                resstr += 'X'*ten
                
        # 大于5
        if lessnum>=5:
            if lessnum>=9:
                lessnum = lessnum - 9
                resstr += 'IX'
            else:
                five = int(lessnum/5)
                lessnum = lessnum - five*5
                resstr += 'V'*five
                
        # 大于1
        if lessnum>=1:
            if lessnum>=4:
                lessnum = lessnum - 4
                resstr += 'IV'
            else:
                resstr += 'I'*lessnum

        return resstr