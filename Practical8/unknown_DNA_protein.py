import re
name=input('Input the file name here(example: unknown_function.fa):')
og_file=open(name,'r')
new_file=open('Unknown DNA to protein.fa','w')
#create the gencode dictionary
gencode = {
    "TTT":'F',"TTC":'F',"TTA":'L',"TTG":'L',
    "TCT":'S',"TCC":'S',"TCA":'S',"TCG":'S',
    "TAT":'Y',"TAC":'Y',"TAA":'O',"TAG":'U',
    "TGT":'C',"TGC":'C',"TGA":'X',"TGG":'W',
    "CTT":'L',"CTC":'L',"CTA":'L',"CTG":'L',
    "CCT":'P',"CCC":'P',"CCA":'P',"CCG":'P',
    "CAT":'H',"CAC":'H',"CAA":'Q',"CAG":'Z',
    "CGT":'R',"CGC":'R',"CGA":'R',"CGG":'R',
    "ATT":'I',"ATC":'I',"ATA":'J',"ATG":'M',
    "ACT":'T',"ACC":'T',"ACA":'T',"ACG":'T',
    "AAT":'N',"AAC":'B',"AAA":'K',"AAG":'K',
    "AGT":'S',"AGC":'S',"AGA":'R',"AGG":'R',
    "GTT":'V',"GTC":'V',"GTA":'V',"GTG":'V',
    "GCT":'A',"GCC":'A',"GCA":'A',"GCG":'A',
    "GAT":'D',"GAC":'D',"GAA":'E',"GAG":'E',
    "GGT":'G',"GGC":'G',"GGA":'G',"GGG":'G',}
#define two value
outputs = ''
amino_acid = ''
for line in og_file:
    #similar to what i did in finding unknown function. use regular expression to search in line start with '>'
    if line.startswith('>'):
        output = re.search(r'>(.+?)\s',line)
        output = output[0]
    else:
        seq = re.findall('...',line)
#calculate the length of amino acids
        for i in range(len(seq)):
            if gencode[seq[i]] != (r'O|U|X'):
                amino_acid = amino_acid + gencode[seq[i]]
            else:
                break
        length = len(amino_acid)
        outputs = outputs + ('>' + output + '     ' + str(length) + '\n' + amino_acid + '\n')
        amino_acid = ''
    
og_file.close()
new_file.write(outputs)
new_file.close()
# below is another way to show the results, which is more convinient that file for me to see if there are problems in my code.
file = open('Unknown DNA to protein.fa','r')
print(file.read())
