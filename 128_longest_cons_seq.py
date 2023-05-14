class Solution:
    def longestConsecutive(self, nums):
        
        # use set for optimal solution
        
        numSet = set(nums)
        longest_seq = 0
        
        for i in nums:
            if i-1 not in numSet:
                temp_length = 0
                while i+temp_length in numSet:
                    temp_length +=1
                longest_seq = max(longest_seq,temp_length)
                
        return longest_seq
                
        
        
        
        
        
        
nums = [100,4,200,1,3,2]       
obj = Solution()
print(obj.longestConsecutive(nums))