# Calculate Expected offsprings (CEO)

class CEO:

    def __init__(self, couple_list):
        self.couple_list = couple_list

        """"
        0. AA with AA -> 100% dominant 
        1. AA with Aa -> 100% dominant 
        2. AA with aa -> 100% dominant 
        3. Aa with Aa -> 75% dominant 
        4. Aa with aa -> 50% dominant 
        5. aa with aa -> 0% dominant 

        """

    def expected_offspring(self):

        genotype_dom_ratio = {0: 1, 1: 1,  2: 1, 3: 0.75, 4: 0.5, 5: 0 }
        # key is the index in couple_list
        # value is the dominant ratio from couples (see docstring)
        expected_num = 0 

        for index, couples in enumerate(self.couple_list):

            if couples > 0:
                expected_num += couples * genotype_dom_ratio[index]

        return 2 * expected_num # for two offprings 

########################################################## Unit test #################################################################

import unittest
from Project_13 import CEO

class Test_CEO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.obj = CEO([16983,17683,16162,16541,19008,18923])

    def test_expected_offspring(self):

        self.assertEqual(self.obj.expected_offspring(), 145475.5)

if __name__ == "__main__":
    unittest.main()

    
