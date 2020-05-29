class MF_law:
    dictionary = {}
    population = 0
    dom_count = 0
    def __init__(self):
        self.dictionary[("HH/HH"), ("HH/Hh"), ("HH/hh")] = 1
        self.dictionary["Hh/Hh"] = 3/4
        self.dictionary["Hh/hh"] = 2/4
    
    def calc_prob(self,k, m, n):
        # HH - homozygous dominant
        # Hh - heterozygous 
        # hh - homozygous recessive
        self.population = k + m + n
        wout_replace = self.population - 1 
        first_prob = k/self.population # you pick HH
        second_prob = m/self.population # you pick Hh
        third_prob = n/self.population # you pick hh

        # homozygous dominant
        self.dom_count += (first_prob * ((k-1)/(wout_replace))) # HH mate w/ HH
        self.dom_count += (first_prob * (m/wout_replace)) # HH mate w/ Hh
        self.dom_count += (first_prob * (n/wout_replace)) # HH mate w/ hh

        # heterozygous
        self.dom_count += (second_prob * (k/wout_replace)) # Hh mate w/ HH
        self.dom_count += (second_prob * ((m-1)/(wout_replace)) * (3/4)) # Hh mate w/ Hh
        print((second_prob * ((m-1)/(wout_replace)) * (3/4)))
        self.dom_count += (second_prob * (n/wout_replace) * (1/2)) # Hh mate w/ hh

        # homozygous recessive
        self.dom_count += (third_prob * (k/wout_replace)) # hh mate w/ HH
        self.dom_count += (third_prob * (m/wout_replace) * (1/2)) # hh mate w/ Hh
        self.dom_count += (third_prob * ((n-1)/(wout_replace)) * 0) # hh mate w/ hh

        return self.dom_count

obj = MF_law()
print(obj.calc_prob(k, m, n))

