class counting_PM:
    list_0 = []
    list_1 = []
    count = 0

    def __init__(self):

        file = open("sample.txt", "r")
        seq = file.read()
        string_0, string_1 = seq.split("\n", 2)
        word = zip(string_0, string_1)
       
        for x, y in word:
            if(x != y):
                self.count+=1

        print(self.count)
           
obj = counting_PM()

