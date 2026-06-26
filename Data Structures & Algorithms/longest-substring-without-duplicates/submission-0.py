class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        l, r = 0, 0
        temp = ""

        while r < len(s):
            if s[r] not in temp:
                temp += s[r]
                maxi = max(maxi, len(temp))
                r += 1
            else:
                temp = temp[1:]
                l += 1
        
        return maxi
