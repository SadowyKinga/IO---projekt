import unittest
from unittest import mock
import Jak_dojade
import tkinter as tk

class FakeTk:
    def call(self, *args, **kwargs):
        pass

    def createcommand(self, *args, **kwargs):
        pass

class FakeMaster:
    def __init__(self):
        self._title = ''
        self._config = None
        self.tk = FakeTk()
        self._last_child_ids = None
        self._w = '.'
        self.children = {}

    def title(self, *args, **kwargs):
        pass

    def config(self, *args, **kwargs):
        pass
    
    def geometry(self, *args, **kwargs):
        pass
    
    def resizable(self, *args, **kwargs):
        pass
       
class SecondPageTest(unittest.TestCase):
    def setUp(self):
        self.page = Jak_dojade.Second_page(FakeMaster(), 1)
        
    '''test, gdy brak danego połączenia'''                   
    def test_nr_1__show_lines_when_no_connection_exists(self):
        config_mock = mock.Mock()
        config_mock.config = mock.Mock()
        self.page.connect_to_data  = lambda x, y, z: []

        with mock.patch('tkinter.Label') as mock_label:
            mock_label.return_value = config_mock
            self.page.show_lines('a', 'b', 'c')
            config_mock.config.assert_called_once_with(text="")
            
    '''test, gdy istnieje dane połączenie'''
    def test_nr_2_show_lines_when_connection_exists(self):
        config_mock = mock.Mock()
        config_mock.config = mock.Mock()
        self.page.connect_to_data  = lambda x, y, z: ['line1', 'line2', 'line3']

        with mock.patch('tkinter.Label') as mock_label:
            mock_label.return_value = config_mock
            self.page.show_lines('a', 'b', 'c')
            config_mock.config.assert_called_once_with(text="'line1', 'line2', 'line3'")          
            
    '''test, odpowiedź użytkownika - między punktem A i B.'''
    def test_nr_3_users_answers(self):
        config_mock = mock.Mock()
        config_mock.config = mock.Mock()
        expected_answers = ['Student place', 'From place', 'To place']
        self.page.student_place = mock.Mock()
        self.page.student_place.get.return_value = expected_answers[0]
        
        self.page.from_place = mock.Mock()
        self.page.from_place.get.return_value = expected_answers[1]
        
        self.page.to_place = mock.Mock()
        self.page.to_place.get.return_value = expected_answers[2]

        with mock.patch('tkinter.Label'):
            answers = self.page.get_user_answers()
            self.assertEqual(expected_answers, answers)

    '''test dla połączeń linie między sąsiednimi parami przystanków'''
    def test_nr_4_making_graph_from_file_text(self):
        text = {'14': ['Rondo Grzegórzeckie', 'Teatr Variété'], 
                '13': ['Park Wodny', 'Tondosa'] }
        expected_dict = {'Park Wodny': {'Tondosa': ['13']},
                        'Rondo Grzegórzeckie': {'Teatr Variété': ['14']}, 
                        'Teatr Variété': {}, 'Tondosa': {}}
        new_dict = self.page.making_graph_from_file_text(text)
        self.assertEqual(expected_dict, new_dict)
    
            
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
    suite = unittest.TestLoader().loadTestsFromTestCase(SecondPageTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    suite = unittest.TestLoader().loadTestsFromTestCase(FindPathTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
