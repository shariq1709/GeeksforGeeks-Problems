class Solution:
    def factorial(self, n):
        product = 1
        for i in range(1, n + 1):
            product *= i
        return [int(digit) for digit in str(product)]