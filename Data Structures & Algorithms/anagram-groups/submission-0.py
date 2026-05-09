class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for p in strs:
            key = "".join(sorted(p))

            group[key].append(p)


        return list(group.values())