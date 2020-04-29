class Transcribe:

    RNA_string = ""
    DNA_string = ""

    def __init__(self):

        file = open("Transcribe.txt", "r")

        for x in file:

            self.RNA_string += x

        self.DNA_string = self.RNA_string.replace("T", "U", -1) 

        print(self.DNA_string)

obj = Transcribe()
