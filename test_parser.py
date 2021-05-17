import unittest
import os

import file_parser

class TestFileParserOnComma(unittest.TestCase):
    def setUp(self):
        self.parser = file_parser.FileParser(",")
        self.test_files_root = './test_files'
    
    def test_parse_and_get_persons(self):
        file_to_results = {
            'comma1.txt': [
                file_parser.Person("Abercrombie", "Neil", "Male", "Tan", "2/13/1943"),
                file_parser.Person("Bishop", "Timothy", "Male", "Yellow", "4/23/1967"),
                file_parser.Person("Kelly", "Sue", "Female", "Pink", "7/12/1959")
            ],
            'comma2.txt': [
                file_parser.Person("Abercrombie", "Neil", "Female", "Tan", "2/13/1943"),
                file_parser.Person("Kelly", "Sue", "Female", "Pink", "7/12/1959"),
                file_parser.Person("Bishop", "Timothy", "Female", "Yellow", "4/23/1967")
            ],
            'comma3.txt': [
                file_parser.Person("Bishop", "Timothy", "Male", "Yellow", "4/23/1967"),
                file_parser.Person("Abercrombie", "Neil", "Male", "Tan", "4/23/1967"),
                file_parser.Person("Kelly", "Sue", "Female", "Pink", "7/12/1959")
            ]
        }

        for file, result in file_to_results.items():
            persons = self.parser.parse_and_get_persons(
                os.path.join(self.test_files_root, file))
            self.assertListEqual(persons, result)


class TestFileParserOnPipe(unittest.TestCase):
    def setUp(self):
        self.parser = file_parser.FileParser("|")
        self.test_files_root = './test_files'
    
    def test_parse_and_get_persons(self):
        file_to_results = {
            'pipe1.txt': [
                file_parser.Person("Smith", "Steve", "M", "Red", "3-3-1985", "D"),
                file_parser.Person("Bonk", "Radek", "M", "Green", "6-3-1975", "S"),
                file_parser.Person("Bouillon", "Francis", "M", "Blue", "6-3-1975", "G")
            ],
            'pipe2.txt': [
                file_parser.Person("Bond", "Steve", "M", "Red", "3-3-1985", "D"),
                file_parser.Person("Bonk", "Radek", "M", "Green", "6-5-1985", "S"),
                file_parser.Person("Bouillon", "Francis", "M", "Blue", "6-3-1975", "G")
            ],
            'pipe3.txt': [
                file_parser.Person("Bonk", "Steve", "M", "Red", "6-3-1975", "D"),
                file_parser.Person("Bonk", "Radek", "M", "Green", "6-3-1975", "S"),
                file_parser.Person("Bonk", "Francis", "M", "Blue", "6-3-1975", "G")
            ]
        }

        for file, result in file_to_results.items():
            persons = self.parser.parse_and_get_persons(
                os.path.join(self.test_files_root, file))
            self.assertListEqual(persons, result)


class TestFileParserOnSpace(unittest.TestCase):
    def setUp(self):
        self.parser = file_parser.FileParser(" ")
        self.test_files_root = './test_files'
    
    def test_parse_and_get_persons(self):
        file_to_results = {
            'space1.txt': [
                file_parser.Person("Kournikova", "Anna", "F", "Red", "6-3-1975", "F"),
                file_parser.Person("Hingis", "Martina", "F", "Green", "4-2-1979", "M"),
                file_parser.Person("Seles", "Monica", "F", "Black", "12-2-1973", "H"),
            ],
            'space2.txt': [
                file_parser.Person("Kournikova", "Anna", "F", "Red", "6-3-1975", "F"),
                file_parser.Person("Hingis", "Martin", "M", "Green", "4-2-1979", "M"),
                file_parser.Person("Seles", "Monica", "F", "Black", "12-2-1973", "F"),
            ],
            'space3.txt': [
                file_parser.Person("Kournikova", "Anna", "F", "Red", "6-3-1975", "F"),
                file_parser.Person("-", "Martina", "F", "Green", "4-2-1979", "M"),
                file_parser.Person("Seles", "Monica", "F", "Black", "12-2-1973", "H"),
            ]
        }

        for file, result in file_to_results.items():
            persons = self.parser.parse_and_get_persons(
                os.path.join(self.test_files_root, file))
            self.assertListEqual(persons, result)
