# one liner caesar cipher
# 07/22/2022 - 14:50 (utc+8) @noteve

# sample input
string = "PyTHon Caesar CiPHer"

[print(string.translate({ord(c):(x:=(96,64)[c.isupper()])+(26,y:=(ord(c)-x+shift)%26)[y!=0] if c!=' ' else 32 for c in string}), ' '*4, f'[{shift}]') for shift in [*range(31), *range(-1,-31,-1)]]
