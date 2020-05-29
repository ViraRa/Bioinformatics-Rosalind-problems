class Mortal_Wabbits:
# dynamic programming 
    
    memo = []
    dying_gen = 0

    def __init__(self, n, m):
        a_sub_0 = 0
        a_sub_1 = 1
        self.memo.append(a_sub_0) #index 0
        self.memo.append(a_sub_1) #index 1, starting off with a small pair of rabbits
        
        self.dying_gen = m + 1
        print(self.rabbit_recurrence(n, m))
    
    def rabbit_recurrence(self, n, m):

        for x in range(2, n+1): # this is "n+1" because I want to include the nth generation

            if(x > self.dying_gen): # this generation will suffer rabbit loss
                self.memo.append(self.memo[x-1] + self.memo[x-2] - self.memo[x - (m+1)]) 
                # This is the previous two generation 
                # minus the portion of rabbits after mth month or x - (m+1) 
            if(x == self.dying_gen):
                self.memo.append(self.memo[x-1] + self.memo[x-2] - 1) 
                # to be explict here I wrote this as a reurrence relation. 
                # This can be simplified as the previous generation 
                # since a pair of rabbits die off starting from previous gen.
            if(x <= m): # no dying rabbits here
                self.memo.append(self.memo[x-1] + (self.memo[x-2])) 
                # in the beginning evaluate as a normal fib. sequence
        return self.memo[-1]

obj = Mortal_Wabbits(90,19) #this took a lot of thinking ... 

