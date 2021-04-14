#Task3
class student():
    def __init__(self,name,code_portfolio,poster_presentation,final_exam):
        self.name=name
        self.code_portfolio=code_portfolio
        self.poster_presentation=poster_presentation
        self.final_exam=final_exam
#get all the information into one sentence
    def output(self):
        return (int(self.code_portfolio)*(4/10)+int(self.poster_presentation)*(3/10)+int(self.final_exam)*(3/10))
#here is the example
x='Zhu Keying'
y='90'
z='80'
w='70'
C=student(x,y,z,w)
print('Here is the emample(the grades i ues are code_portfolio:90,poster_presentation:80,final_exam here:70 ):')
print('student name:'+x+'   '+'student grade:'+str(C.output()))
#code below is wrote for other users, here is used to ask users to input the information
x=input('Please write name here:')
y=int(input('Please write Student grade for the code_portfolio here:'))
z=int(input('Please write Student grade for the poster_presentation:'))
w=int(input('Please write Student grade in the final_exam here:'))
C=student(x,y,z,w)
print('student name:'+x+'   '+'student grade:'+str(C.output()))

