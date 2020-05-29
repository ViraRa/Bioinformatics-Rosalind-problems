import itertools
class Translating_RNA:

    protein = ""
    Code = {}
    RNA = ""
    RNA_list = [] # this list seperate RNA into codons
    nuc = ["U", "C", "A", "G"]
    key = []

    def __init__(self):

        file = open("sample.txt", "r")
        self.RNA = file.read()

        for y in range(0, len(self.RNA), 3):
            self.RNA_list.append(self.RNA[y:y+3])
       
        # find all the 3 letter possibilities in nuc list
        for z in itertools.product(self.nuc, repeat=3):
            self.key.append("".join(z))

        for x in range(0, 64, 1):
            if(x == 0 or x == 1):
                self.Code[self.key[x]] = "F"
            elif(x == 2 or x == 3 or x in range(16,20)):
                self.Code[self.key[x]] = "L"
            elif(x in range(4,8) or x in range(44, 46)):
                self.Code[self.key[x]] = "S"
            elif(x == 8 or x == 9):
                self.Code[self.key[x]] = "Y"
            elif(x == 12 or x == 13):
                self.Code[self.key[x]] = "C"
            elif(x == 15):
                self.Code[self.key[x]] = "W"
            elif(x in range(20, 24)):
                self.Code[self.key[x]] = "P"
            elif(x == 24 or x == 25):
                self.Code[self.key[x]] = "H"
            elif(x == 26 or x == 27):
                self.Code[self.key[x]] = "Q"
            elif(x in range(28,32) or x in range(46, 48)):
                self.Code[self.key[x]] = "R"
            elif(x in range(32, 35)):
                self.Code[self.key[x]] = "I"
            elif(x == 35):
                self.Code[self.key[x]] = "M"
            elif(x in range(36,40)):
                self.Code[self.key[x]] = "T"
            elif(x == 40 or x == 41):
                self.Code[self.key[x]] = "N"
            elif(x == 42 or x == 43):
                self.Code[self.key[x]] = "K"
            elif(x in range(48,52)):
                self.Code[self.key[x]] = "V"
            elif(x in range(52,56)):
                self.Code[self.key[x]] = "A"
            elif(x == 56 or x == 57):
                self.Code[self.key[x]] = "D"
            elif(x == 58 or x == 59):
                self.Code[self.key[x]] = "E"
            elif(x in range(60,64)):
                self.Code[self.key[x]] = "G"

    def translate(self):
        for x in self.RNA_list:
            if(x in self.Code.keys()):
                self.protein += self.Code.get(x)
            else:
                pass # for completeness
        return self.protein

obj = Translating_RNA()
print(obj.translate())

