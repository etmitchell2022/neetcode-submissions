class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        word_map = {}

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in word_map:
                word_map[sorted_str].append(string)
            else:
                word_map[sorted_str] = [string]
        
        for key, value in word_map.items():
            result.append(value)

        return result