# Enumerating gene order (EGO)
import math 
import itertools
class EGO:

    def __init__(self, num):
        
        self.n = num

    def permutation(self):

        perm = math.factorial(self.n) / (self.n - (self.n - 1)) # proper way

        return int(perm)
    
    def gene_order(self):

        int_str = "" # contains consecutive number from 0 to self.n

        for i in range(1, self.n+1):int_str += str(i)

        for order in list(itertools.permutations(int_str, self.n)):
            perm_order = "".join(order)
            print(perm_order.replace("", " ", -1))

        

obj = EGO(5)
print(obj.permutation())
obj.gene_order()


