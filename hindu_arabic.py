# one liner roman numerals to hindu arabic with random roman numerals generator
# 07/18/2022 - 01:35 (utc+8) @noteve


# generating random roman numerals for inputs (also one liner lol)
inputs = (lambda _,ch,rn,lst:sorted(set([''.join(l for g in lst[:n][::-1] for l in ch([g[0]*rn(1,3), g[1]+g[0]*rn(1,3),g[0]+g[1],g[0]+g[2]],weights=[30,30,20,20])[0] if l!='x') for n in [1,2,None] for _ in range(100)]),key=len))(m:=__import__('random'), m.choices, m.randint,['IVX','XLC','CDM','Mxx'])


# roman numerals to hindu arabic conversion
[(lambda vals,r: print(r, '--', sum([vals[r[i]] * (1,-1)[vals[r[i]]<vals[r[i+1]]] for i in range(len(r)-1)])+vals[r[-1]]))({s:n for s,n in zip('IVXLCDM',[1,5,10,50,100,500,1000])},roman) for roman in inputs]
