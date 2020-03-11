class Solution:
    def myAtoi(self, str: str) -> int:
        flist = []
        flag = 0
        for i in str:
            if i.isdigit():
                flist.append(i)
                flag+=1
            elif i.isdigit()==False:
                if i==' ':
                    if flag==0:
                        continue
                    else:
                        break
                elif (i=='-' or i=='+') and flag==0:
                    flist.append(i)
                    flag += 1
                else:
                    break
        finalstr = ''.join(flist)
        if finalstr != '' and finalstr != '-' and finalstr != '+':
            finalstr = int(finalstr)
        else:
            finalstr = 0
        try:
            assert -2**31 <= finalstr <= 2**31 -1
        except:
            if finalstr > 0:
                finalstr = 2**31 -1
            else:
                finalstr = -2**31
        return finalstr
