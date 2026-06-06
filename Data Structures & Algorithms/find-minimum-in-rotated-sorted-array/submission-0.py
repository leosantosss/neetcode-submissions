class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1 

        answer = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                answer  = min(answer, nums[l])
                break

            mid = (l+r) // 2
            answer = min(answer, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return answer