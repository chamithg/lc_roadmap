class Solution:
    def trap(self, height):
        
        if len(height)< 3:
            return 0
        trapped = 0
        lp = 0
        mh = max(height)
        for i in range(len(height)-1):
            if height[i] >= height[lp]:
                lp = i
            if height[i] == mh:
                mh = max(height[i+1:])                
            trapped += max(0,min(height[lp],mh)- height[i])
        return trapped

            

height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj = Solution()
obj.trap(height)