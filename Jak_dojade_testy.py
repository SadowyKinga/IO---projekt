'''  Tests for MPK.py '''

import unittest
import Jak_dojade
       
class FindPathTest(unittest.TestCase):
    ''' Running tests for find_shortest_path_function'''
    def setUp(self):  
        self.graf = {'pktA':{'pktB':['1', '2'], 'pktD':['7', '8']},
                    'pktB':{'pktD':['9', '11']},
                    'pktD':{'pktA':['11', '12'],'pktC':['89', '83']},
                    'pktC':{'pktA':['3', '7']}
                    }

    def test_nr_1_find_shortest_path_first(self):
        self.result1 = 'pktA, pktB'
        self.assertEqual(Jak_dojade.find_shortest_path(self.graf,'pktA','pktB'),
                                                         (self.result1))

    def test_nr_2_find_shortest_path_second(self):
        self.result2 = 'pktB, pktD, pktC'
        self.assertEqual(Jak_dojade.find_shortest_path(self.graf,'pktB','pktC'),
                                                         (self.result2))
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FindPathTest)
    unittest.TextTestRunner(verbosity=2).run(suite)