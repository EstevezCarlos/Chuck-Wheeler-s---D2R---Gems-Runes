import unittest as ut
from main import Transformer as T


class SimpleExcelFlow(ut.TestCase):
    source_path = 'test/source.xlsx'
    matrix = [['Name', 'Birth'], ['Tomi', 2014], ['Iwo', 2017]]
    dict = {
            'Tomi': {'Name': 'Tomi', 'Birth': 2014},
            'Iwo': {'Name': 'Iwo', 'Birth': 2017},

        }
    tsv_string = (
        'Name	Birth\n'+
        'Tomi	2014\n'+
        'Iwo	2017\n'
    )
    def test_excel_to_matrix(self):
        self.assertEqual(T.excel_to_matrix(self.source_path), self.matrix)

    def test_matrix_to_dict(self):
        self.assertEqual(T.matrix_to_dicts(self.matrix), self.dict)

    def test_dicts_to_tsv_string(self):
        self.assertEqual(T.dicts_to_tsv_string(self.dict), self.tsv_string)


class SimpleCsvFlow(ut.TestCase):
    original_path = 'test/original.tsv'
    dict = {
            'Tomi': {'Name': 'Tomi', 'Birth': "1014"},
            'Iwo': {'Name': 'Iwo', 'Birth': "2017"},
            'Asia': {'Name': 'Asia', 'Birth': "1982"},

        }
    tsv_string = (
        'Name	Birth\n'+
        'Tomi	1014\n'+
        'Iwo	2017\n'+
        'Asia	1982\n'
    )
    def test_csv_to_dict(self):
        self.assertEqual(T.csv_to_dicts(self.original_path), self.dict)

    def test_dicts_to_tsv_string(self):
        self.assertEqual(T.dicts_to_tsv_string(self.dict), self.tsv_string)

class Merging(ut.TestCase):
    mod_dict = {
        'Tomi': {'Name': 'Tomi', 'Birth': 2014, 'BadKey': 'Tallbird'},
        'Iwo': {'Name': 'Iwo', 'Birth': 2017, 'BadKey': 'Technics'},
    }
    original_dict = {
        'Tomi': {'Name': 'Tomi', 'Initials': 'TK', 'Birth': "1014"},
        'Iwo': {'Name': 'Iwo', 'Initials': 'IK', 'Birth': "2017"},
        'Asia': {'Name': 'Asia', 'Initials': 'JK', 'Birth': "1982"},
    }
    expected_dict = {
        'Tomi': {'Name': 'Tomi', 'Initials': 'TK', 'Birth': 2014},
        'Iwo': {'Name': 'Iwo', 'Initials': 'IK', 'Birth': 2017},
        'Asia': {'Name': 'Asia', 'Initials': 'JK', 'Birth': "1982"},
    }
    def test_merge_dicts(self):
        T.merge_dicts(self.original_dict,self.mod_dict)
        self.assertEqual(self.original_dict, self.expected_dict)




if __name__ == '__main__':
    ut.main()