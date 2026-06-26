class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = [0] * 26
        for i in s1:
            arr[ord(i) - 97] += 1

        l = 0
        n = len(s1)          # changed from len(s1) - 1
        r = l + n - 1      # changed

        while r < len(s2):
            temp = arr.copy()  # changed from temp = arr
            found = True

            for i in range(l, r + 1):  # changed to include r
                ch = s2[i]

                if temp[ord(ch) - 97] > 0:
                    temp[ord(ch) - 97] -= 1
                else:
                    found = False
                    break

            if found:
                return True       # changed from true

            l += 1                # changed (move window)
            r = l + n - 1         # changed

        return False