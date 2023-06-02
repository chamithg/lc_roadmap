class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        def map(pos1,pos2,arr1,arr2):
            p1 = pos1
            p2 = pos2
            while p1 <= len(arr1)-1 and arr1[p1] <= arr2[p2]:
                outArr.append(arr1[p1])
                p1+=1
            if p1== len(arr1):
                for i in range(p2,len(arr2)):
                    outArr.append(arr2[i])
                return
            else:        
                map(p2,p1,arr2,arr1)
        
        def getMed(arr):
            if len(arr)%2 == 0:
                return (arr[len(arr)//2-1] + arr[(len(arr)//2)])/2
            else:
                return arr[len(arr)//2]

        if not nums1:return getMed(nums2)
        if not nums2:return getMed(nums1)
        
        if nums1[0]< nums2[0]:
            first = nums1
            second = nums2
        else:
            first = nums2
            second = nums1
        outArr = []
        

        
        map(0,0,first,second)
        return getMed(outArr)
            

nums1 = [1,2]
nums2 = [3,4]
obj = Solution()
print(obj.findMedianSortedArrays(nums1,nums2))