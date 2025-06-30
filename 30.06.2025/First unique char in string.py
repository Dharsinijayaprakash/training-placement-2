class Solution:
    def firstUniqChar(self, s):
        from collections import Counter
        
        count = Counter(s)
        
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        
        return -1
