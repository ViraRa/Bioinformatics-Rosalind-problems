from collections import defaultdict
import sys

class Diagraph: # may contain cycles | if no cycles then it is called a DAG or directed acyclic graph

    def __init__(self, k):

        # reading the file and put the labels and seq in a list

        if(k < 0 or not isinstance(k,int)):
            print("\nk should be an integer and greater than zero.\n")
            print("Please try again\n")
            sys.exit(0)

        file_string = ""
        labels = []
        seq = []
        with open("Graph.txt", "r") as file:
            file_string = file.read().split(">")

        del file_string[0] # always empty

        for x in range(0, len(file_string)):
            labels.append(file_string[x][:13]) # only works if the label is fixd and has 13 char in it
            seq.append(file_string[x][13:].strip("\n")) # this only works if the label has 13 char in it
            seq[x] = seq[x].replace("\n", "") # getting rid of all new line character

        unformated_answer = self.adj_list(labels, seq, k)

        formated_answer = self.format(unformated_answer)

        print(formated_answer)

    @staticmethod   
    def adj_list(IDs_list, seq_list, k):

        adj_list = defaultdict(list) # to allow duplicate keys due to list append
        # defaultdictonary is similar to regular dictionary but does not raise a keyerror if key is not found
        v = 0
        w = v + 1
        seq_list_no_dup = []

        for x in range(0, len(seq_list)): # removing duplicates in both ID_list and seq_list
            if(seq_list[x] not in seq_list_no_dup):
                seq_list_no_dup.append(seq_list[x])
            else:
                key = x
                del IDs_list[x]
        
        label_and_seq = list(zip(IDs_list, seq_list_no_dup)) # this for easier retrieval of label
        # I can do zip because both lists are the same size
        # create an adj_list where the nodes are the strings in seq_list
        # match the first string suffix  of size k to the second string prefix of size k 
        # first string should not match with second string
        # return the label or ID of strings the meet the req in adj_list format

        # append both string s's label and string t's label for easier formating
        while w < len(label_and_seq):

            if (v == len(label_and_seq)): # exit condition
                break
            
            if(v == 0):
                if(label_and_seq[v][1][-k:] == label_and_seq[w][1][:k] and label_and_seq[v][1] != label_and_seq[w][1]): # checking if the prefix == suffix of size k
                    if(label_and_seq[v-1][0] != label_and_seq[w][0]): 
                        # edge case, don't want previous key equal current value  
                        adj_list[label_and_seq[v][0]].append((label_and_seq[v][0], label_and_seq[w][0]))
            else: # v and w switch places after v increment so w is v now and v is w now
                if(label_and_seq[w][1][-k:] == label_and_seq[v][1][:k] and label_and_seq[v][1] != label_and_seq[w][1]): # checking if the prefix == suffix of size k
                   if(label_and_seq[w-1][0] != label_and_seq[v][0]): 
                       # edge case, don't want previous key equals current value  
                        adj_list[label_and_seq[w][0]].append((label_and_seq[w][0], label_and_seq[v][0]))
            
            
            if(w == len(label_and_seq) - 1):
                v += 1
                w = 0
            w += 1

        value = list(adj_list.values())
               
        return value

    @staticmethod
    def format(ans):

        # formating the answer to look like Rosalind output
        formated_answer = ""
        temp = ""
        x = 0
        
        while x < len(ans):
            if(len(ans[x]) == 1):
                formated_answer += " ".join(ans[x][0]) + "\n"
            else:
                for y in range(0, len(ans[x])):
                    formated_answer += " ".join(ans[x][y]) + "\n"
            x += 1

        return formated_answer

obj = Diagraph(3) 
# k is always three, but to make my program more scalable I ask the user to input an k
