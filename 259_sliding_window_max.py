class Solution:
    def maxSlidingWindow(self, nums, k) :
        output = []
        
        test_list = sorted(list(set(nums[0:k])))
        for i in range(k,len(nums)+1):
            output.append(max(nums[i-k:i]))
            
        

        print(test_list)
        return output
        
        

nums = [1,3,-1,-3,5,3,6,7]
k = 3
obj = Solution()
print(obj.maxSlidingWindow(nums,k))