class Reverse_Complement():

    string = ""
    reverse_string = ""
    comp_strand = ""

    def __init__(self):

        file = open("sample.txt", "r")

        for x in file:

            self.string += x
        
        file.close()
        self.reverse_string = self.string[::-1] # reverse a string by splicing

    def comp_seq(self):

        for y in self.reverse_string:
            
            if(y != "None" and y == "A"):
                self.comp_strand += "T"
            elif(y != "None" and y == "T"):
                self.comp_strand += "A"
            elif(y != "None" and y == "C"):
                self.comp_strand += "G"
            elif(y != "None" and y == "G"):
                self.comp_strand += "C"

        return self.comp_strand
