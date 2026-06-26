class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        l = 0
        maxi = 0
        res = 0

        for r in range(len(s)):
            arr[ord(s[r]) - 65] += 1
            maxi = max(maxi, arr[ord(s[r]) - 65])
            while (r-l+1)-maxi > k:
                arr[ord(s[l]) - 65] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
