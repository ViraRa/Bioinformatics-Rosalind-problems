class Compute_GC:
    def __init__(self):

        file = open("GC.txt", "r")
        dictionary = {}
        name_list = []
        string = file.read().split(">")
        # first one will always be empty
        answer = {}

        for i in range(1, len(string)):

            name = string[i].split("\n", 1)[0]
            name_list.append(name)
            seq = string[i].split("\n", 1)[1]
            dictionary[name] = seq
        
        for x in name_list:

            y = self.calc_GC(dictionary.get(x))
            answer[y] = x

     
        maximum = max(answer.keys())
        print(answer.get(maximum)) # label
        print(maximum) # max %GC

    def calc_GC(self, seq):
        
        length = 0 # length of sequence without newline char

        for z in seq: # seq contains newline char. 
            if(z != "\n"):
                length += 1

        count = 0 # number of G or C occurrences in seq

        for y in range(0, len(seq)):

            if(seq[y] == "G" or seq[y] == "C"):
                count += 1

        percentage = (count/length) * 100
        return percentage


        
obj = Compute_GC()


