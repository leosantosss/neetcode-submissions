class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        while j > i:
            currentSum = numbers[j] + numbers[i]
            if currentSum > target:
                j -= 1
            elif currentSum < target:
                i += 1
            else:
                return [i+1,j+1]

            

            


            
            

            

            

            
            

                

