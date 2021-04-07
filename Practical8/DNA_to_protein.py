import re
seq="ATGCGACTACGATCGAGGGCC"
l=len(seq)
a=l/3
P=""
while a>0:
    n=0
    A=seq[0:3]
    dict={}
    protein={"ATG":"M","CGA":"R","CTA":"L","TCG":"S","AGG":"R","GCC":"A"}
    p=protein[A]
    seq=seq[3:]
    P=P+p
    a=a-1
print(P)

