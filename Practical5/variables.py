#Here is the task--Some simple math.input all of the data.
a=030702
b=190784
c=100321
d=abs(a-c)
print(d)
e=abs(a-b)
print(e)
if d>e:
  print("d is greater")
else:
  print("e is greater")



#Here is the task--Booleans.let X equals to True, Y equals to False.
X=bool(1)
Y=bool(0)
Z=(X and not Y)or(Y and not X)
if Z==True:
  print("True")
else:
  print("False")
W=(X!=Y)
if Z==W:
  print("Z==W")
else:
  print("Z!=W")

