"""
Need to break into parts.
1. Sort the string based on length
2. find the longest common substring with the two smallest string: O(n * m)
3. Repeat step 2 until end of DNA sequence using the LCS from step 2

"""
import numpy as np
# SM - Shared Motif
class SM:

    def __init__(self):
        
        self.seq = []
        self.label = ""

    def read_fasta(self):

        with open("smotif.txt", "r") as file:
            self.label = file.read().split(">")
            del self.label[0] # always empty

            for x in range(0, len(self.label)):
                self.seq.append(self.label[x][10:].strip("\n")) # this only works if the label has 10 char in it
                self.seq[x] = self.seq[x].replace("\n", "") # getting rid of all new line character
        
    
        self.seq.sort(key=len) # Inplace sort based on length
        return self.seq
    
    # Longest common sequence algo
    def LCS(self, string1, string2):

        m = len(string1)
        n = len(string2)

        LCS_matrix = np.zeros(shape=(m+1, n+1)) # initializing all zeros 

        # main algo
        # if there is a match between characters then go up in main diagonal element and add one
        # No match? element is zero
        for row in range(0, LCS_matrix.shape[0]):
            for col in range(0, LCS_matrix.shape[1]):
                if row == 0 or col == 0:
                    LCS_matrix[row, col] = 0
                elif string1[row - 1] == string2[col - 1]:
                    LCS_matrix[row, col] = LCS_matrix[row-1, col-1] + 1
                else:
                    LCS_matrix[row, col] = 0
        
        result_string = ""
        
        # if the matrix is all zero then there isn't a common substring
        if np.all(LCS_matrix == 0):
            print("There is not common substring")
            return 
        
        index = np.where(LCS_matrix == np.max(LCS_matrix))
        max_row = index[0][0]
        max_col = index[1][0]
        # format is array([row...]), array([col...])
        # taking the first pair of row and col 
        
        
        # getting the longest common substring from matrix
        # will need to reverse it
        while LCS_matrix[max_row][max_col] != 0: # Worst Case: traverse the entire main diagonal O((N*M)/2)

            result_string += string1[max_row-1]
            max_row, max_col = max_row - 1, max_col - 1

        return result_string[::-1]
    
    # run LCS function until there a common pattern in all strings
    def find_pattern(self, pattern):

        # starting at 2 since already matched index 0 and 1
        for i in range(2, len(sorted_seq)):  # 2 ... N for loop is O(N)
            pattern = obj.LCS(pattern, sorted_seq[i]) # LCS is O(N + M + (N*M)/2)

        # Total complexity is O(N^2 * NM * (N^2*M)/2)
        
        # If M == N  then O(N^2 * N^2 * N^3/2) therefore O(0.5 * x^7) in the worst case

        # Polynomial run time although it's a little slow
        
        return pattern # returning the first LCS
           
obj = SM()
sorted_seq = obj.read_fasta()
inital_pattern = obj.LCS(sorted_seq[0], sorted_seq[1])
final_pattern = obj.find_pattern(inital_pattern)

####################################################### Unit test for LCS function ######################################################

from Shared_motif import SM
import unittest

class TestSM(unittest.TestCase):

    # testing only the longest common substring function in SM class

    def test_LCS(self):

        test = SM()
        self.assertEqual(test.LCS("AAAAA", "AAA"), "AAA") # same letter case
        self.assertEqual(test.LCS("ACGTACGT", "AACCGTATA"), "CGTA") # different letters case
        self.assertEqual(test.LCS("LCLC", "CLCL"), "LCL") # repeating two letter case

if __name__ == "__main__":
    unittest.main()

    
