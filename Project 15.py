import urllib.request # to grab sequence from uniprot url
from collections import deque
import sys
class PMotif:

    def __init__(self):

        self.uniprot_id = []
        self.location = ""

    def read_ID(self):

        with open("ID.txt", "r") as file:
            self.uniprot_id = file.read().split("\n")
        
        if self.uniprot_id[-1].strip() == "": del self.uniprot_id[-1]
        return self.uniprot_id
    
    
    def check_uniport(self, uniprot_id):

        for ID in uniprot_id:
            answer = self.check_uniport_helper(ID)
            if answer != None:
                print(answer)
    
    
    def check_uniport_helper(self, uniprot_id): # check for N{P}[ST]{P} motif
        fasta = deque([])
        answer = "" # contains the ID and locations

        try:
            with urllib.request.urlopen("https://www.uniprot.org/uniprot/{}.fasta".format(uniprot_id)) as uni:
                
                for line in uni:
                    temp = str(line).strip("b'").strip("\\n")
                    fasta.append(temp)

            if not fasta: # deque is empty because the ID is deleted from uniprot. Return None and move on
                print("bad link")
                return 

            urllib.request.urlcleanup()
        
        except urllib.request.URLError: #URL was not found
            print("URL not found error")
            sys.exit(0)

        fasta.popleft() # don't need the uniprot label
        fasta_string = "".join(fasta)

        for i,_ in enumerate(fasta_string): # Motif is N, not P, S or T, not P (in this order)

            if len(fasta_string[i:i+4]) == 4:# 4 is the length of motif
                if fasta_string[i] == "N":
                    if fasta_string[i+1] != "P" and fasta_string[i+3] != "P":
                        if fasta_string[i+2] == "S" or fasta_string[i+2] == "T":
                            self.location += str(i + 1) + " " # must add 1 since started with 0
                
            
        if self.location.strip() != "": 
            answer =  uniprot_id + "\n" + self.location
            self.location = ""
            return answer
        else: # no motif found then return None and move on
            return 


obj = PMotif()
uniprot_id = obj.read_ID()
obj.check_uniport(uniprot_id)
