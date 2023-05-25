import math
class Solution:
    def minEatingSpeed(self, piles,h):
        maxPile = max(piles)
        minTime = maxPile
        def findK(mid):
            k = 0
            for j in piles:
                k += math.ceil(j/mid)
            return k
        lp = 1
        rp = maxPile
        
        while lp <= rp:
            mid = (rp+lp)//2 
            if findK(mid) > h:
                lp = mid+1
            elif findK(mid)<= h:
                minTime = min(minTime,mid)
                rp = mid-1
        return minTime

piles = [30,11,23,4,20]
h = 6
obj = Solution()
print(obj.minEatingSpeed(piles,h))