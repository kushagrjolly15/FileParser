import unittest
import os

import file_parser

class TestSortPerson(unittest.TestCase):
    def setUp(self):
        self.comma_parser = file_parser.FileParser(",")
        self.space_parser = file_parser.FileParser(" ")
        self.pipe_parser = file_parser.FileParser("|")
        self.test_files_root = './test_files'

    def test_sort_by_gender_and_lastname(self):
        test_case = [
            file_parser.Person("Abercrombie", "Neil", "Male", "Tan", "2/13/1943"),
            file_parser.Person("Kelly", "Sue", "Female", "Pink", "7/12/1959"),
            file_parser.Person("Bishop", "Timothy", "Male", "Yellow", "4/23/1967"),
        ]
        result = [
            file_parser.Person("Kelly", "Sue", "Female", "Pink", "7/12/1959"),
            file_parser.Person("Abercrombie", "Neil", "Male", "Tan", "2/13/1943"),
            file_parser.Person("Bishop", "Timothy", "Male", "Yellow", "4/23/1967")
        ]

        self.assertListEqual(
            file_parser.Person.sort_by_gender_and_lastname(test_case),
            result)
        
        test_case = [
            file_parser.Person("Abercrombie", "Neil", "Female", "Tan", "2/13/1943"),
            file_parser.Person("Kelly", "Sue", "Female", "Pink", "7/12/1959"),
            file_parser.Person("Bishop", "Timothy", "Female", "Yellow", "4/23/1967")
        ]

        result = [
            file_parser.Person("Abercrombie", "Neil", "Female", "Tan", "2/13/1943"),
            file_parser.Person("Bishop", "Timothy", "Female", "Yellow", "4/23/1967"),
            file_parser.Person("Kelly", "Sue", "Female", "Pink", "7/12/1959")
        ]

        self.assertListEqual(
            file_parser.Person.sort_by_gender_and_lastname(test_case),
            result)

        test_case = [
            file_parser.Person("Bonk", "Steve", "M", "Red", "6-3-1975", "D"),
            file_parser.Person("Bonk", "Radek", "M", "Green", "6-3-1975", "S"),
            file_parser.Person("Bonk", "Francis", "M", "Blue", "6-3-1975", "G")
        ]

        result = [
            file_parser.Person("Bonk", "Steve", "M", "Red", "6-3-1975", "D"),
            file_parser.Person("Bonk", "Radek", "M", "Green", "6-3-1975", "S"),
            file_parser.Person("Bonk", "Francis", "M", "Blue", "6-3-1975", "G")
        ]

        self.assertListEqual(
            file_parser.Person.sort_by_gender_and_lastname(test_case),
            result)  
    
    def test_sort_by_dob_and_lastname(self):
        test_case = [
            file_parser.Person("Smith", "Steve", "M", "Red", "3-3-1985", "D"),
            file_parser.Person("Bonk", "Radek", "M", "Green", "6-3-1975", "S"),
            file_parser.Person("Bouillon", "Francis", "M", "Blue", "6-3-1975", "G")
        ]

        result = [
            file_parser.Person("Bonk", "Radek", "M", "Green", "6-3-1975", "S"),
            file_parser.Person("Bouillon", "Francis", "M", "Blue", "6-3-1975", "G"),
            file_parser.Person("Smith", "Steve", "M", "Red", "3-3-1985", "D"),
        ]

        self.assertListEqual(
            file_parser.Person.sort_by_dob_and_lastname(test_case),
            result)
        
        test_case = [
            file_parser.Person("Bond", "Steve", "M", "Red", "3-3-1985", "D"),
            file_parser.Person("Bonk", "Radek", "M", "Green", "6-5-1985", "S"),
            file_parser.Person("Bouillon", "Francis", "M", "Blue", "6-3-1975", "G")
        ]

        result = [
            file_parser.Person("Bouillon", "Francis", "M", "Blue", "6-3-1975", "G"),
            file_parser.Person("Bond", "Steve", "M", "Red", "3-3-1985", "D"),
            file_parser.Person("Bonk", "Radek", "M", "Green", "6-5-1985", "S"),
        ]

        self.assertListEqual(
            file_parser.Person.sort_by_dob_and_lastname(test_case),
            result)
        
        test_case = [
            file_parser.Person("Bonk", "Steve", "M", "Red", "6-3-1975", "D"),
            file_parser.Person("Bonk", "Radek", "M", "Green", "6-3-1975", "S"),
            file_parser.Person("Bonk", "Francis", "M", "Blue", "6-3-1975", "G")
        ]

        result = [
            file_parser.Person("Bonk", "Steve", "M", "Red", "6-3-1975", "D"),
            file_parser.Person("Bonk", "Radek", "M", "Green", "6-3-1975", "S"),
            file_parser.Person("Bonk", "Francis", "M", "Blue", "6-3-1975", "G")
        ]

        self.assertListEqual(
            file_parser.Person.sort_by_dob_and_lastname(test_case),
            result)

    def test_sort_lastname_reversed(self):
        test_case = [
            file_parser.Person("Kournikova", "Anna", "F", "Red", "6-3-1975", "F"),
            file_parser.Person("Hingis", "Martina", "F", "Green", "4-2-1979", "M"),
            file_parser.Person("Seles", "Monica", "F", "Black", "12-2-1973", "H")
        ]

        result = [
            file_parser.Person("Seles", "Monica", "F", "Black", "12-2-1973", "H"),
            file_parser.Person("Kournikova", "Anna", "F", "Red", "6-3-1975", "F"),
            file_parser.Person("Hingis", "Martina", "F", "Green", "4-2-1979", "M")
        ]

        self.assertListEqual(
            file_parser.Person.sort_lastname_reversed(test_case),
            result)

        test_case = [
            file_parser.Person("Kournikova", "Anna", "F", "Red", "6-3-1975", "F"),
            file_parser.Person("-", "Martina", "F", "Green", "4-2-1979", "M"),
            file_parser.Person("Seles", "Monica", "F", "Black", "12-2-1973", "H")
        ]

        result = [
            file_parser.Person("Seles", "Monica", "F", "Black", "12-2-1973", "H"),
            file_parser.Person("Kournikova", "Anna", "F", "Red", "6-3-1975", "F"),
            file_parser.Person("-", "Martina", "F", "Green", "4-2-1979", "M")
        ]

        self.assertListEqual(
            file_parser.Person.sort_lastname_reversed(test_case),
            result)
