# one liner calculator without eval() function
# 07/07/2022 - 22:30 (utc+8) @noteve

# sample input 6+4
n1, n2, op = (6, 4, '+')


(lambda i: print([i.__add__, i.__sub__, i.__mul__, i.__truediv__]['+-*÷'.index(op)](n1,n2)))(int)
