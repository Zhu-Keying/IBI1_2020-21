n=84
r=1.2
count=0
#x stand for the number of student that have been infected
x=1
while count<5:
  count=count+1
  x=x*(r**count)
print("The r rate is "+str(r)+" and the total number of individuals infected after 5 generations is "+str(x))
