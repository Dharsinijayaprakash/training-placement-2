class Solution:
    def addBinary(self, a, b):
        result = ""
        carry = 0
        
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            carry = total // 2
            result = str(total % 2) + result
        
        return result
