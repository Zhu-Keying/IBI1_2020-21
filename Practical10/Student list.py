#Task2
#create a class
class student():
    def __init__(self,first_name,last_name,undergraduate_programme):
        
        self.first_name=first_name
        self.last_name=last_name
        self.undergraduate_programme=undergraduate_programme
#get all the information into one sentence
    def combination(self):
        return ('full name:'+self.last_name+' '+self.first_name+'  '+'undergraduate programme:'+self.undergraduate_programme)
#here is the example
x='Keying'
y='Zhu'
z='BMS'
C=student(x,y,z)
print('Here is the emample:')
print(C.combination())
#code below is wrote for other users, here is used to ask users to input the information
x=input('Please write first name here:')
y=input('Please write last name here:')
z=input('Please write undergraduate programme here:')
C=student(x,y,z)
print(C.combination())

