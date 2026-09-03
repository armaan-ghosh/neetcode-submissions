class Solution:
    def minOperations(self, s: str) -> int:
        operations_for_zero_start = 0

        for i, char in enumerate(s):
            if i % 2 == 0:
                if char != '0':
                    operations_for_zero_start += 1
            else:
                if char != '1':
                    operations_for_zero_start += 1

        operations_for_one_start = len(s) - operations_for_zero_start

        return min(operations_for_one_start, operations_for_zero_start)