import numpy as np
class C:
    def __init__(self):

        matrix = np.array([[]])
        string = "" # split the ">" char in file

        file = open("sample.txt", "r")
        string = file.read().split(">")
        del string[0] # always empty
        seq = []
        file.close()

        for x in range(0, len(string)):
            seq.append(string[x][13:].strip("\n")) # this only works if the label has 13 char in it
            seq[x] = seq[x].replace("\n", "") # getting rid of all new line character
            
        length = len(seq) # size of list
        char_length = len(seq[0])

        matrix = np.full((4, char_length), 0) # initalizing all zeros for now
    
        table = self.make_table(seq, matrix, length, char_length) # returns the 4 by n matrix

        con_seq = self.find_con(table) # returns the consensus sequence

        print(con_seq)
        print("A: " + " ".join(str(x) for x in table[0]))
        print("C: " + " ".join(str(x) for x in table[1]))
        print("G: " + " ".join(str(x) for x in table[2]))
        print("T: " + " ".join(str(x) for x in table[3]))
    
       
        
    def make_table(self, seq, table, size, char_length):
        string = ""
        temp = []
        i = 0
        x = 0

        count_A = 0
        count_C = 0
        count_G = 0
        count_T = 0

        # get the character to align from vertically. See Rosalind example
        while (x < size):
            
            temp.append(seq[x][i])
            x += 1
            if(x == size):
                i += 1
                x = 0
            if(i == char_length):
                temp.append("stop")
                break
       
        x = 0
        row = 0 # acts as a row variable
        col = 0 # acts as a col varaible 

        # filling up the table
        while (temp[x] != "stop"):
            if(col == char_length):
                break
            if(temp[x] == "A"):
                count_A += 1
                table[row][col] = count_A
            elif(temp[x] == "C"):
                count_C += 1
                table[row+1][col] = count_C
            elif(temp[x] == "G"):
                count_G += 1
                table[row+2][col] = count_G
            elif(temp[x] == "T"):
                count_T += 1
                table[row+3][col] = count_T
             
            if(x in range(size-1, len(temp), size)): # this is fine or x == size - 1
                # remember: inlcuding the size - 1
                count_A = 0
                count_C = 0
                count_G = 0
                count_T = 0
                col += 1
            x += 1
        return table

    def find_con(self, matrix):
        # row 0 = A
        # row 1 = C
        # row 2 = G
        # row 3 = T
        max_list = np.amax(matrix, axis=0) # find the max of each column
        i = 0
        row = 0
        col = 0
        con_seq = ""
        temp_list = []

        # get the indices of the maximum element per column
        # where does the 3 come from (2, 3) should be a 6
        while i < matrix.size:
            if(row == 4):
                row = 0
                col += 1
            if(matrix[row][col] == max_list[col]):
                x = (row, col)
                temp_list.append(x)
            if(col == len(max_list)):
                break
            row += 1
            i += 1
        
        count =  len(temp_list) # temp_list contain indices contain indices of max element per column
        second_index = [] # contains the column without duplicates
        temp = [] # contains the columns
        
        # in case there are duplicaties (i.e elements from the same column)
        # if you remove a value then you need to remove the start index too
        for x in range(0, count):
            if (not (temp_list[x][1] in second_index)):
                second_index.append(temp_list[x][1])            
                temp.append(temp_list[x][0])
       
        answer = tuple(zip(temp,second_index))

        for x in range(0, len(answer)):
            if(answer[x][0] == 0):
                con_seq += "A"
            elif(answer[x][0] == 1):
                con_seq += "C"
            elif(answer[x][0] == 2):
                con_seq += "G"
            elif(answer[x][0] == 3):
                con_seq += "T"
        return con_seq                  
obj = C()

