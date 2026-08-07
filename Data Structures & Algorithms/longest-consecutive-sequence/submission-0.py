class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique_nums = set(nums)

        for num in unique_nums:
            if num - 1 not in unique_nums:
                current_num = num
                current_length = 1

                while current_num + 1 in unique_nums:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest