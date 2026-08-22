class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

            if freq[x] >= 2:
                return True

        return False