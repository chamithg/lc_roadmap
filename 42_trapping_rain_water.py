class Solution:
    def trap(self, height):
        
        if len(height)< 3:
            return 0
        trapped = 0
        lp = 0
        rp = height.index(max(height))
        while rp <= len(height):
            for i in range(rp):
                if height[i] >= height[lp]:
                    lp = i
                trapped += min(height[rp],height[lp])- height[i]
            lp = rp
            rp = height.index(max(height[lp+1:]))
        print("hello")
        print(trapped)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj = Solution()
obj.trap(height)