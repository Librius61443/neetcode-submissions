class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while(l <= r):
            mid = (r-l)//2 + l
            tot = 0
            for i in piles:
                tot += math.ceil(i/mid)
            if tot <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res



            