class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # v2
        # return Counter(s) == Counter(t)

        # v1
        if len(s) != len(t):
            return False
        
        cont = {}

        for l in s:
            cont[l] = cont.get(l, 0) + 1

        for l in t:
            if l not in cont:
                return False
            cont[l] -= 1
            if cont[l] < 0:
                return False
        
        return True