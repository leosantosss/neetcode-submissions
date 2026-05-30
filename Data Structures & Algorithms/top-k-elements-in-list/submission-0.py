class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []

        for i in range (len(nums)+1): #because this will actually make it len(nums) long
            freq.append([])
        
        for n in nums:
            count[n] = 1 + count.get(n,0) #get basically gets the value at key n and if it DNE it returns 0
        
        for key,value in count.items():
            freq[value].append(key)

        result = []
        for i in range (len(freq)-1,0,-1):#starts at last index and stops before 0 cuz then no value there
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result