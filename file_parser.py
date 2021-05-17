from datetime import datetime
import argparse

class Person:
    def __init__(self,
                 last_name,
                 first_name,
                 gender,
                 fav_color,
                 dob,
                 middle_initial=None):
        self.__last_name = last_name
        self.__first_name = first_name
        if gender == 'M':
            self.__gender = "Male"
        elif gender == 'F':
            self.__gender = "Female"
        else:
            self.__gender = gender
        self.__fav_color = fav_color
        if '-' in dob:
            self.__dob = datetime.strptime(dob, '%m-%d-%Y')
        else:
            self.__dob = datetime.strptime(dob, '%m/%d/%Y')
        self.__middle_initial = middle_initial
    
    def __eq__(self, other_person):
        res = self.__last_name == other_person.__last_name
        res = res and self.__first_name == other_person.__first_name
        res = res and self.__gender == other_person.__gender
        res = res and self.__dob == other_person.__dob
        res = res and self.__middle_initial == other_person.__middle_initial
        res = res and self.__fav_color == other_person.__fav_color
        
        return res

    @classmethod
    def sort_by_gender_and_lastname(cls, persons):
        gender_to_bool = lambda gender: gender == "Male"

        def sorting_key(person):
            return gender_to_bool(person.__gender), person.__last_name

        return sorted(persons, key=sorting_key)

    @classmethod
    def sort_by_dob_and_lastname(cls, persons):
        def sorting_key(person):
            return person.__dob, person.__last_name
        
        return sorted(persons, key=sorting_key)

    @classmethod
    def sort_lastname_reversed(cls, persons):
        def sorting_key(person):
            return person.__last_name
        
        return sorted(persons, key=sorting_key, reverse=True)

    def __str__(self):
        return f'{self.__last_name}, {self.__first_name}, {self.__gender}, {self.__dob.strftime("%m/%d/%Y")}, {self.__fav_color}'
    
    def __repr__(self):
        return self.__str__()

class FileParser:
    def __init__(self, delimiter=' '):
        self.__delimeter = delimiter
    
    def parse_and_get_persons(self, file):
        with open(file) as f:
            lines = f.readlines()
        
        persons = []
        for line in lines:
            props = line.strip().split(self.__delimeter)
            props = [prop.strip() for prop in props]
            
            if self.__delimeter == ' ':
                persons.append(self.__space_delim(props))
            elif self.__delimeter == ',':
                persons.append(self.__comma_delim(props))
            elif self.__delimeter == '|':
                persons.append(self.__pipe_delim(props))
            else:
                raise AttributeError()
        
        return persons

    def __comma_delim(self, props):
        return Person(props[0], props[1], props[2], props[3], props[4])

    def __space_delim(self, props):
        return Person(
            props[0], props[1], props[3], props[5], props[4], props[2])

    def __pipe_delim(self, props):
        return Person(
            props[0], props[1], props[3], props[4], props[5], props[2])


def display_persons_list(persons):
    for person in persons:
        print(person)

def main(file, delimiter):
    parser = FileParser(delimiter)
    persons = parser.parse_and_get_persons(file)
    print("Given Data:")
    display_persons_list(persons)

    print("\n Sorted by Gender and Last Name:")
    display_persons_list(Person.sort_by_gender_and_lastname(persons))
    print("\n Sorted by DoB and Last Name:")
    display_persons_list(Person.sort_by_dob_and_lastname(persons))
    print("\n Sorted by Last Name in descending order:")
    display_persons_list(Person.sort_lastname_reversed(persons))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-file", help="Path to the file to be parsed")
    argparser.add_argument(
                    "-delimiter",
                    help="""Delimiter used, default ',' 
                            if using '|' or ' ' please use \"|\" and
                            \" \" respectively.""", default=',')
    args = argparser.parse_args()
    main(args.file, args.delimiter)
