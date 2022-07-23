# one liner roman numerals conversion
# 07/06/2022 - 01:45 (utc+8) @noteve
# input: random integers from 1 to 3999


(lambda r,c:[print(f'{num} -->',(lambda nums:''.join([(lambda s,f:[f:=f.replace(b,r) for b,r in{'0':s[0],'1':s[1],'2':s[2]}.items()][2])('IVXLCDMnn'[(len(nums)-1-i)*2:],['','0','00','000','01','1','10','100','1000','02'][nums[i]]) for i in range(len(nums))]))([int(d) for d in f'{num}']))for num in sorted([c([r(1,200),r(1,3999)]) for _ in range(50)])])(__import__('random').randint, __import__('random').choice)
