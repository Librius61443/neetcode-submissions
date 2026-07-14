class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            dist = -(math.sqrt(x**2 + y**2))
            heapq.heappush(maxheap, [dist, x, y])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        res = []
        for i in maxheap:
            dist, x, y = i
            res.append([x, y])
        
        return res
        