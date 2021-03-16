a=["USA","India","Brazil","Russia","UK"]
b=[29862124,11285561,11205972,4360823,4234924]
infection=dict(zip(a,b))
c,d,e,f,g=infection.values()
C,D,E,F,G=infection.keys()
t=c+d+e+f+g
import numpy as np
m=np.array([c,d,e,f,g])
n=np.array([t,t,t,t,t])
r=np.true_divide(m,n)
q=np.array([C,D,E,F,G])
rate=dict(zip(q,r))
print(rate)
import matplotlib.pyplot as plt
labels=q
sizes=r
explode=(0,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
plt.axis("equal")
plt.show()
