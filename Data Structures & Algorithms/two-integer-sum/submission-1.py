class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # v1
        i = -1
        for n1 in nums:
            i += 1
            j = -1
            for n2 in nums:
                j += 1
                if i == j:
                    continue
                if (n1 + n2) == target:
                    return [i,j]
        
        
        return None