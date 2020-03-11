class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 暴力求解 超时
        # maxarea = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area = (j-i) * min(height[i],height[j])
        #         if area > maxarea:
        #             maxarea = area
        # return maxarea

        # 双指针法
        maxarea = 0
        i,j = 0,len(height)-1
        while i<j:
            if height[i]<height[j]:
                area = (j-i)*height[i]
                i+=1
            else:
                area = (j-i)*height[j]
                j-=1
            if area > maxarea:
                maxarea = area
        return maxarea