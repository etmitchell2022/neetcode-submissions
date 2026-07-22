class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        num_map = {}

        for num in nums:
            if num in num_map:
                num_map[num] = num_map[num] + 1
            else:
                num_map[num] = 1

        pairs = num_map.items()

        sorted_items = sorted(
            pairs,
            key=lambda pair: pair[1],
            reverse=True
        )

        top_k = sorted_items[:k]

        for pair in top_k:
            result.append(pair[0])

        return result