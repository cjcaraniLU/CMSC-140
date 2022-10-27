import random
import matplotlib.pyplot as plt

def generate_dna(tablenum):

    random.seed(tablenum)

    dna = ['A','C','G','T']

    seq = "".join(random.choices(dna, k=300))

    # replace start with a start codon
    seq = "TAC" + seq[3:]

    # replace any premature stop codons with non-stops
    seq = seq.replace("ATT", "CAG")
    seq = seq.replace("ATC", "GGA")
    seq = seq.replace("ACT", "AAA")

    # Add in a stop codon somewhere towards the end
    stops = ["ATT", "ATC", "ACT"]
    rand_end = 3 * (random.randint(250,300)//3)
    seq = seq[0:rand_end] + random.choice(stops) + seq[rand_end+3:]

    return seq



print("")



dummyList = list((generate_dna(2)))





for x in range(len(dummyList)):
    
    if (dummyList[x]=="A"):
       dummyList[x]="U"
    elif (dummyList[x]=="C"):
        dummyList[x]="G"
    elif (dummyList[x]=="G"):
        dummyList[x]="C"
    elif(dummyList[x]=="T"):
        dummyList[x]="A"
print("")



joinStr = "".join(dummyList)
print(joinStr)




# =======================================================================================


aa = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP",
    "UGU": "Cys", "UGC": "Cys", "UGA": "STOP", "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}


print("")

emptyList = []
y = 0
    
    
for i in  range (0, len(joinStr), 3):
    
    emptyList.append(joinStr[i:i+3])
    
result = ""

for q in  emptyList:
        
        if(aa[q]!= "STOP"):
            result += "-"+ aa[q]
        else:
           break 
            
print(result)            


#plt.hist(result, bins = len(set(result)))
#plt.show()