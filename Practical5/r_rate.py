n=84
r=1.2
count=5
#x stand for the number of student that have been infected
x=1
x=x*(r**count)
#x is no larger than n
if x>n:
  x=n
print("The r rate is "+str(r)+" and the total number of individuals infected after 5 generations is "+str(x))
