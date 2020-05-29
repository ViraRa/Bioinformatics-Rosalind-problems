class Wabbits:
    a_sub_0 = 0
    a_sub_1 = 1
    memo = []

    def __init__(self):

        self.memo.append(self.a_sub_0) #index 0
        self.memo.append(self.a_sub_1) #index 1

    def rabbit_recurrence(self, n, k):

        for x in range(2, n):

            self.memo.append(k * self.memo[x-2] + (self.memo[x-1]))

        return self.memo
    
obj = Wabbits()
print(obj.rabbit_recurrence(n,k))

