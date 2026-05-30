class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        result = 0

        for num in nums:
            current = num
            streak = 0
            while current in store:
                current += 1
                streak += 1
            result = max(result,streak)

        return result


    
        
        
