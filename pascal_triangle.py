# one liner pascal's triangle
# 07/07/2022 - 15:45 (utc+8) @noteve

(lambda f:[(print(' '.join('%3s'%i for i in f[1:-1]).center(38)),f:=[0,*[x+y for x,y in zip(f,f[1:])],0]) for _ in range(10)])([0,1])
