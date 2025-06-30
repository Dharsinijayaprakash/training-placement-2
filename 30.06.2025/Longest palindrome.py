class Solution:
    def longestPalindrome(self, s):
        from collections import Counter
        
        count = Counter(s)
        length = 0
        odd_found = False
        
        for char_count in count.values():
            length += (char_count // 2) * 2  # Add even part of count
            if char_count % 2 == 1:
                odd_found = True
        
        if odd_found:
            length += 1  # One odd character can go in the middle
        
        return length
