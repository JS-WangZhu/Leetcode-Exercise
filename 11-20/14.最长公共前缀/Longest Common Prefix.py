class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxpre = ''
        try:
            min_length = len(strs[0])
            for i in strs:
                if len(i) < min_length:
                    min_length = len(i)
            loop_times = min_length
            for j in range(loop_times):
                #j是第几位数字，0开始
                sum=0
                for i in range(1,len(strs)):
                    if list(strs[0])[j]==list(strs[i])[j]:
                        sum+=0
                    else:
                        sum+=1
                if sum==0:
                    maxpre+=list(strs[0])[j]
                else:
                    break
        except:
            pass
        return maxpre