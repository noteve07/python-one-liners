# one liner fibonacci sequence
# 07/02/2022 - 13:00 (utc+8) @noteve

(lambda a,b,c:[print([(a:=b),(b:=c),(c:=a+b)][0]) for _ in range(50)])(0,1,1)
