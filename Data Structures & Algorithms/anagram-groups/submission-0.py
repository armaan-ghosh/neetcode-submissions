class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        key = []

        for word in strs:
            sorted_key = ''.join(sorted(word))
            
            if sorted_key in final:
                final[sorted_key].append(word)
            else:
                final[sorted_key] = [word]
        return list(final.values())