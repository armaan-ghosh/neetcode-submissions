class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            num = nums[i]

            result[i] = prefix
            prefix *= num

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            
            result[i] *= postfix
            postfix *= num

        return result