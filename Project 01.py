class counting_DNA_nucleotide:
    string = ""
    def __init__(self):

        try:
            file = open("sample.txt", "r")
        except FileNotFoundError:
            print("File cannot be found")

        for x in file:
            self.string += x

        num_A = self.string.count("A")
        num_G = self.string.count("G")
        num_C = self.string.count("C")
        num_T = self.string.count("T")

        print(str(num_A) + " " + str(num_C) + " " + str(num_G) +  " " + str(num_T))

obj = counting_DNA_nucleotide()

