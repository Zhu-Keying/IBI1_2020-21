#import some modules
import re
import os
import matplotlib.pyplot as plt
import xml.dom.minidom
from xml.dom.minidom import parse

#It's hard for me to finish it individually. So my classmates and I share a similar idea to solve problems.

#get all the element from the file go_obo.xml
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
#the dictionary is create to contain all the ids of terms
dic = {}
#get the id in every term
for term in terms:
    id_node = term.getElementsByTagName('id')[0].childNodes[0].data
    dic[id_node] = []
for term in terms:
    id = term.getElementsByTagName('id')
    is_a = term.getElementsByTagName('is_a')
    for ia in is_a:
            dic[ia.firstChild.data].append(id[0].firstChild.data)
#since the way to treat specific items are same, function can reduce a lot of repeated works!
#(shortage)   the way i use to count use much of time for that it is a one by one step.


#this function is used to find specific words.
def count(specificitems):# specificitems stands for specific items like 'DNA','RNA'...
    global Z
    for term in terms:
        if specificitems in term.getElementsByTagName('defstr')[0].firstChild.data:
            i_d = term.getElementsByTagName('id')[0].firstChild.data
            if dic[i_d]:
                counter=dic[i_d]
                n=node(counter)
                Z=str(n)
    return Z

#this function is used to store
def node(counter):
    for z in range(len(counter)):
        if counter[z] not in store:
            store.append(counter[z])
            node(dic[counter[z]])
    return len(store)

#Get the number of specific items
#DNA
store=[]
DNA=count('DNA')
#RNA
store=[]
RNA=count('RNA')
#!!!!!Protein and protein!!!!!
store=[]
protein1=count('Protein')
store=[]
protein2=count('protein')
proteins=str(int(protein1)+int(protein2))
#carbohydrate
carbohydrate = count('carbohydrate')
#output the results
print('The number of childnodes of DNA is:'+DNA)
print('The number of childnodes of RNA is:'+RNA)
print('The total  number of protein is:'+proteins)
print('The number of carbohydrate is: ' + carbohydrate)

#Draw the pie chart with data
explode = (0, 0, 0, 0.1)
sizes=[DNA,RNA,proteins,carbohydrate]
labels = ("DNA", "proteins", "RNA", "Carbohydrate")
plt.pie(sizes, explode=explode,labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('Child Nodes of 4 macromolecules')
plt.show()



