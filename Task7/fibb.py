#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""

    def get_nth_term(self, n):
        if n <= 0: return 0
        if n == 1: return 1
        
        n1, n2 = 0, 1
        for _ in range(2, n + 1):
            n1, n2 = n2, n1 + n2
        return n2

    def get_divisible_terms(self, n, m):
        divisible_list = []
        n1, n2 = 0, 1
        
        for i in range(n):
            if n1 % m == 0:
                divisible_list.append(n1)
            
            n1, n2 = n2, n1 + n2
            
        return divisible_list

fib_tool = Fibonacci()

N = 100
M = 7

nth_term = fib_tool.get_nth_term(N)

divisible_terms = fib_tool.get_divisible_terms(N, M)

print(f"The {N}-th Fibonacci term is: {nth_term}")
print(f"Fibonacci numbers divisible by {M}: {divisible_terms}")

