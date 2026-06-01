class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #pair (temp,index)
        warmer_days_ahead = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp,index = stack.pop()
                warmer_days_ahead[index] = i - index
            stack.append((t,i))
            
        return warmer_days_ahead
             