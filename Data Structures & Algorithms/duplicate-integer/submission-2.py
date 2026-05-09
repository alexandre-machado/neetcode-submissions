class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # v2
        return len(set(nums)) < len(nums)
        # v1
        map = {}
        for n in nums:
            if n in map:
                return True
            map[n] = True
        return False