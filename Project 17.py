# Open reading frame = 6 per DNA sequence
import itertools
import re
class ORF:

    def __init__(self):

        self.protein = ""
        self.code = {}
        self.nuc = ["U", "C", "A", "G"]
        self.ORF = []
    
    # create codon table
    def create_table(self):

        # another way of doing this is read for an excel file containing the codon table (you write less code this way)
        # I created the table using my previous my code from the translate mRNA question

        # find every possible combination 3 letters long in self.nuc
        for z in itertools.product(self.nuc, repeat=3): 
            self.code["".join(z)] = ""

        for i, key in enumerate(self.code.keys()):
            if i == 0 or i == 1:
                self.code[key] = "F"
            elif i == 2 or i == 3 or i in range(16,20):
                self.code[key] = "L"
            elif i in range(4,8) or i in range(44, 46):
                self.code[key] = "S"
            elif i == 8 or i == 9:
                self.code[key] = "Y"
            elif i == 12 or i == 13:
                self.code[key] = "C"
            elif i == 15:
                self.code[key] = "W"
            elif i in range(20, 24):
                self.code[key] = "P"
            elif i == 24 or i == 25:
                self.code[key] = "H"
            elif i == 26 or i == 27:
                self.code[key] = "Q"
            elif i in range(28,32) or i in range(46, 48):
                self.code[key] = "R"
            elif i in range(32, 35):
                self.code[key] = "I"
            elif i == 35:
                self.code[key] = "M"
            elif i in range(36,40):
                self.code[key] = "T"
            elif i == 40 or i == 41:
                self.code[key] = "N"
            elif i == 42 or i == 43:
                self.code[key] = "K"
            elif i in range(48,52):
                self.code[key] = "V"
            elif i in range(52,56):
                self.code[key] = "A"
            elif i == 56 or i == 57:
                self.code[key] = "D"
            elif i == 58 or i == 59:
                self.code[key] = "E"
            elif i in range(60,64):
                self.code[key] = "G"
            elif key == "UAG" or key =="UGA" or key == "UAA":
                self.code[key] = "stop"
    
    def translate(self, DNA):

        temp_protein = ""
        i = 0

        RNA = DNA.replace("T", "U", -1)
        RNA = RNA + "end" + RNA[1:-1] + "end" + RNA[2:-1]   
        RNA_seq = RNA.split("end") # end indicate unique reading frames

        three_letter = [] #  contains three letter code

        for seq in RNA_seq:
            for i in range(0, len(seq), 3):
                three_letter.append(seq[i:i+3])
            three_letter.append("end")  # end indicate unique reading frames

        for codon in three_letter:
            if codon in self.code.keys():
                temp_protein += self.code.get(codon)
            if codon == "end":
                temp_protein += "end" # end indicate unique reading frames

        # split "end" to indicate separate protein from reading frame
        self.protein = temp_protein.split("end")

        # will always be empty since the last entry was "end" thus splitting it will result in an empty string
        del self.protein[-1] 
    
    def reverse_complement(self, DNA):

        reverse_DNA = DNA[::-1]
        complement_DNA = ""

        for nuc in reverse_DNA:
            if nuc == "A":
                complement_DNA += "T"
            elif nuc == "T":
                complement_DNA += "A"
            elif nuc == "C":
                complement_DNA += "G"
            elif nuc == "G":
                complement_DNA += "C"
        
        return complement_DNA
        
      
    # find the protein strings starting with M until "stop"
    def new_proteins(self):

        # goal is to find all indices of M
        # then slice them using the indices as start till "stop"

        pro_indices = [] # contains the strings with Ms and the their starting indices

        for pro_str in self.protein:
            for i in re.finditer("M", pro_str):
                pro_indices.append((pro_str, i.start())) # i.start() outputs indices that start with M

        if not pro_indices: # nothing in pro_indices
            return None

        for pro_str, ind in pro_indices:
            if pro_str.find("stop", ind) != -1:
                self.ORF.append(pro_str[ind:pro_str.find("stop", ind)])
        return self.ORF
    

# rc ---> reverse complement
all_ORF = ""

with open("ORFDNA.txt", "r") as file:
    _, DNA = file.read().split("\n", 1)
    DNA = DNA.replace("\n", "")


# For DNA
obj = ORF()
obj.create_table()
obj.translate(DNA)
first_three_ORF = obj.new_proteins()

# For rc_DNA
obj_2 = ORF()
obj_2.create_table()
rc_DNA = obj_2.reverse_complement(DNA)
obj_2.translate(rc_DNA)
last_three_ORF = obj_2.new_proteins()

# finding unique ORFs from first three and last three reading frames and printing them
if first_three_ORF != None or last_three_ORF != None: temp = first_three_ORF + last_three_ORF
uniq_ORF = list(dict.fromkeys(temp))

for pro in uniq_ORF: print(pro)
