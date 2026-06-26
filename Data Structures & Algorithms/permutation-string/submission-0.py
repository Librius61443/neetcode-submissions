class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = [0] * 26

        for ch in s1:
            arr[ord(ch) - 97] += 1

        window = len(s1)

        for l in range(len(s2) - window + 1):
            temp = arr.copy()
            found = True

            for i in range(l, l + window):
                idx = ord(s2[i]) - 97

                if temp[idx] > 0:
                    temp[idx] -= 1
                else:
                    found = False
                    break

            if found:
                return True

        return False