"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def add_numbers(file:list, tel_numbers:set):
    """
    Given a file adds all available numbers into a set
    inputs
    param file: file containing telephone numbers
    param tel_numbers: variable used to contain the telephone numbers
    output
    return: tel_numbers with file numbers extracted
    """
    for column in [0, 1]:
        temp_numbers = [data[column] for data in file]
        print(len(temp_numbers))
        # accepts another iterable & ignor the same elements
        tel_numbers.update(temp_numbers)
    return tel_numbers


if __name__ == "__main__":
    tel_numbers = set()

    tel_numbers = add_numbers(calls, tel_numbers)
    tel_numbers = add_numbers(texts, tel_numbers)

    print("There are {} different telephone numbers in the records.".format(len(tel_numbers)))


