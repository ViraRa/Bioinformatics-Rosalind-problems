# RT -> Reverse Translate
# O(N) time complexity
import itertools
class RT:

    def __init__(self):

        self.protein = ""
        self.code = {}
        self.nuc = ["U", "C", "A", "G"]

    def codon_table(self):

        # another way of creating the table is to read from an excel file containing the codon table (you write less code this way)
        # I created the table using my previous my code from the translate mRNA question.

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

    # count the possible codon per aa 
    def reverse_translate_count(self):

        RNA_length = 1
        temp_key = []

        with open("RT.txt", "r") as file:
            protein = file.read()
        
        for aa in protein:
        
            if aa in self.code.values():
                RNA_length *= list(self.code.values()).count(aa)
        
        
        return (RNA_length * 3) % 1_000_000 # the 3 represents the possible stop codons (UAG, UAA, UGA)

    
obj = RT()
obj.codon_table()
print(obj.reverse_translate_count())
