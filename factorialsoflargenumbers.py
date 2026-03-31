class Solution:
    def factorial(self, n):
        result = [1]
        
        for i in range(2, n + 1):
            carry = 0
            
            for j in range(len(result)):
                prod = result[j] * i + carry
                result[j] = prod % 10
                carry = prod // 10
            
            while carry:
                result.append(carry % 10)
                carry //= 10
        
        # digits are stored in reverse
        result.reverse()
        return result
