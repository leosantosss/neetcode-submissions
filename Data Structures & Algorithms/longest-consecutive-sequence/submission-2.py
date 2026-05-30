class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence = 0
        for n in nums:
            count = 1
            if (n-1) not in nums_set:
                while(n+count) in nums_set:
                    count +=1
        
            if count > max_sequence:
                max_sequence = count
        
        return max_sequence

    







    
        
        
