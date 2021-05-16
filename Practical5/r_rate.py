#input all of the data
n=84
r=1.2
# use x to count the rounds
x=1
p=False
while p==False:
    p=True
    x=x+1
    n=n*r+n
    if x<6:
        p=False
#use "str()" to change the type of the data ,then print all the information out
print("The r rate is "+str(r)+" and the total number of individuals infected after 5 generations is "+str(n))

