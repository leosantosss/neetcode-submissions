class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the length of s is the same as the length of t cuz then its false
        if len(s) != len(t):
            return False
        #create two dicts for each letter in the strings
        s_dict = {}
        t_dict = {}

        for letter in s:#going through each letter and adding it and its count into dict
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
        for key in s_dict:#going through the dict and checking that they exist in t dict
            if key in t_dict:
                if s_dict.get(key) == t_dict.get(key):
                    continue
                else:
                    return False
            else:
                return False
        return True