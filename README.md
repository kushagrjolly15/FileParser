# File Parsing

The given take home assignment helps parse different data structures based on the delimiter 
and file attributes. The code for the assignment can be found in `file_parser.py`.

## Working with the code
The code assumes that a file with a particular delimiter will have data in a particular order.

```
Example:
A file with delimiter comma (',') will have data in order - 
LastName, FirstName, Gender, FavoriteColor, DateOfBirth

A file with delimiter pipe ('|') will have data in order - 
LastName | FirstName | MiddleInitial | Gender | FavoriteColor | DateOfBirth

A file with delimiter space (' ') will have data in order - 
LastName FirstName MiddleInitial Gender DateOfBirth FavoriteColor
```

To parse a file and see the possible sorting we can use the following command line helps:

```
usage: file_parser.py [-h] [-file FILE] [-delimiter DELIMITER]

optional arguments:
  -h, --help            show this help message and exit
  -file FILE            Path to the file to be parsed
  -delimiter DELIMITER  Delimiter used, default ',' if using '|' or ' ' please use "|" and " " respectively.
```

So to run a file say `comma.txt` which is in same directory and have delimiter comma (','), we have to run the following command:

`python file_parser.py -file comma.txt -delimiter ,`

## Unit Tests
The given submission also includes unit tests for the `file_parser.py`. The test for the parser which converts file data to needed data structure is tested via `test_parser.py`. The test for the sorting algorithms which sorts via given strategies is tested using `test_sort.py`.

### Edge Cases considered
I considered many edge cases such as:
- All persons being of same gender
- Overlapping date of births 
- Last name as '-'
- Same last name and date of births combination

### Run Test cases
To run test cases use:
```
python -m unittest test_parser.py
python -m unittest test_sort.py
```