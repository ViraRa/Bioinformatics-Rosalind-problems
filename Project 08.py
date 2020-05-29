#Knuth Morris Pratt (KMP) patten algo - O(N)
# Amazing algo!
import numpy as np
class motif_in_DNA:
    s = "" # text
    t = "" # pattern

    # trying to avoid using global variables since they decrease performance slightly

    def __init__(self):

        file = open("sample.txt", "r")
        string = file.read()
        self.s, self.t = string.split("\n", 2)
        file.close()
        
    def KMP_search(self):
        # a = len(self.t) # length of patthen
        # b = len(self.s) # length of text

        i = 1 # temp index for string
        j = 0 # temp index for pattern
        arr_lps = np.array([])
        
        arr_lps = self.lps_array()

        while i <= len(self.s): # better to start at one to avoid confusion
            if(self.t[j] != self.s[i-1]): # mismatch 
                # the below code is very similar to the lps_array code if j != 0
                if(j != 0):
                    j = int(arr_lps[j - 1]) # Why? you already checked the char before j. Now check after
                else: 
                    i += 1
            else: # match found!
                i += 1
                j += 1

                # This is a rosalind problem now. I need to return the occurrences of the patten in s
                if(j == len(self.t)):
                    print(str(i-j))
                    # need to reset j
                    j = int(arr_lps[j - 1])

    def lps_array(self): #O(N)
        length = len(self.t)
        lps = np.array([])
        lps = np.insert(lps, 0, 0) # index 0 is always 0
        i = 1 
        j = 0 
        
        while i < length:
            if(self.t[j] != self.t[i]):
                if (j != 0):
                    j = int(lps[j-1]) # find new j. Why? You want to separate j from i to find the
                    # longest prefix
                else:   # j == 0
                    lps = np.insert(lps, i, j) # inserting j at the ith postion in lps
                    # For above, you already checked between i and j and found no match
                    i += 1 # you have to move i since you can't move j
            
            else:
                lps = np.insert(lps, i, j+1)
                i += 1
                j += 1
            
        return lps

obj = motif_in_DNA()
obj.KMP_search()


