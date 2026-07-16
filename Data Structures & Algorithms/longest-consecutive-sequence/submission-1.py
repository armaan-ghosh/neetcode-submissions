class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)

        current_length = 0
        longest = 0

        for n in numbers:
            if n - 1 not in numbers:
                current_num = n
                current_length = 1

                while current_num + 1 in numbers:
                    current_num += 1
                    current_length += 1

            longest = max(longest, current_length)

        return longest