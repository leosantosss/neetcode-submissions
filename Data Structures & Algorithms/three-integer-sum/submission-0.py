class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i,k in enumerate(nums):
            if k > 0:
                break
            
            l = i +1
            r  = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while r > l:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum < 0:
                    l += 1
                elif currentSum > 0:
                    r -= 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                    
        return result

                




            


            
                


