class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        grouped = []
        for i in range(len(strs)):# looping through words in main list
            if i in grouped:
                continue
            current = {}
            word = strs[i]
            sublist = [word]
            for j in range(len(strs[i])):# looping through letters in current word
                if strs[i][j] in current:
                    current[strs[i][j]] += 1
                else:
                    current[strs[i][j]] = 1
            
            for k in range(i+1,len(strs)): # looping through words to compare to
                if k in grouped:
                    continue
                other = {}
                other_word = strs[k]
                if len(other_word) != len(word):
                    continue
                for h in range(len(strs[k])):# looping through letters in comparing word
                    if strs[k][h] in other:
                        other[strs[k][h]] += 1
                    else:
                        other[strs[k][h]] = 1
                
                check = True

                for key in current:#checking dictionaries between current and other word
                    if key not in other:
                        check = False
                        break
                    if current.get(key) != other.get(key):
                        check = False
                        break
                if check:
                    sublist.append(other_word)
                    grouped.append(i)
                    grouped.append(k)

            answer.append(sublist)
        return answer            
                
                
