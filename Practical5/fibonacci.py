# may be i need three variables. x and y are used to make sum. z is used to transfer the origin number of y
count=13
x=1
y=1
#first, print out the first two numbers.
print(x)
print(y)
#build a loop with count.
while count>2:
  count=count-1
  z=y
  y=x+y
  x=z
  print(y)  
