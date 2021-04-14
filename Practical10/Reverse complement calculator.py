#Task1
def f(x):
#change all the lower case to upper case
    x1 = x.upper()
    l=list(x1)
    dict = {}
    converts= {'A':'T','T':'A','G':'C','C':'G'}
#conversts elements in the list 
    x2= [converts[a] for a in l]
#reverse its order
    x3 = x2[::-1]
#connect all the elements
    o=''.join(x3)
    return o
#here is the example,the sequence i input is 'actgtgACTG'
x='actgtgACTG'
print('Here is the emample，the sequence i input is actgtgACTG：')
print(f(x))
#ask to input a sequence
x=input('please input your sequence:')
print(f(x))






