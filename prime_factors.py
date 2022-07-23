# one liner prime factors (a challenge)
# 07/21/2022 - 10:40 (utc+8) @noteve

# sample input: 1980
num = 1980


(lambda n: print([con:=(type(n)==int and 2<=n<=1_000_000), n:=(1,n)[con], lst:=[0], t:=len([(lst.append(1),n:=n//2)[1] for _ in lst if n%2==0]), l:=([[(lst.append(1),n:=n//i,i)[2] for _ in lst if n%i==0] for i in range(3, n+1, 2) if n%i==0]),' x '.join(p:=[(f'{x[0]}', f'{x[0]} ^ {len(x)}')[len(x)>1] for x in l][::-1])+('',' x ')[len(p)>0 and t>0]+('','2',f'2 ^ {t}')[(t>0)+(t>1)], 'ValueError'][(6,5)[con]]))(num)
