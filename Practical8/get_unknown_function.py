import re
u=open("/Users/zhukeying/IBI1_2020-21/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
output=open("/Users/zhukeying/IBI1_2020-21/Practical8/unknown_function.fa","w")
name=''
seq=''
length=0
x=0
printout=False
for line in u:
    if line.startswith(">"):
            if 'unknown function' in line:
                if x!=0:
                    output.write(f'{name:30}'+str(length)+'\n'+seq)
                name=re.search(r'>([^ ]+)_mRNA',line).group(1)
                seq=""
                length=0
                printout=True
                x=x+1
            else:
                printout=False
    else:
        if printout==True:
            seq=seq+line
            length=length+len(line)-1
output.write(f'{name:30}'+str(length)+'\n'+seq)
u.close()
output.close()
