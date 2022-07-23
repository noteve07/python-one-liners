# one liner collatz conjecture
# 07/04/2022 - 12:00 (utc+8) @noteve
# sample input = 50
n = 50


# version 1 (list comprehension)
(lambda x:[(print([f'{x}÷2 = {x//2}',f'{x}×3+1 = {x*3+1}'][x%2]),x:=(x//2,x*3+1)[x%2]) for i in range(x*5) if x>1])(n)


# version 2 (while loop)
while n>1:(lambda x,y:print([f'{x}÷2 = {x//2}', f'{x}×3+1 = {x*3+1}'][x%2]))(x:=n,n:=(n//2,n*3+1)[n%2])
