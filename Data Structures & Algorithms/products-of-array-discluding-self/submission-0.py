class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        prefix = 1

        for index in range(len(nums)):
            output[index] = prefix
            prefix *= nums[index]

        postfix = 1

        for index in range(len(nums) - 1, -1, -1):
            output[index] *= postfix
            postfix *= nums[index]

        return output