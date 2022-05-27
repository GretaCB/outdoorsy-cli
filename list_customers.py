#!/usr/bin/env python

import argparse
import inquirer
import os
import sys

from typing import List, Iterable
from inquirer import Path



class Customer:
    def __init__(self, name, email, vehicle_type, vehicle_name, vehicle_length):
        self.name = name
        self.email = email
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.vehicle_length = vehicle_length

    def __repr__(self):
        return f'Customer({self.name!r}, {self.email!r}, {self.vehicle_type!r}, {self.vehicle_name!r}, {self.vehicle_length!r})'


def getName(customer):
    """
    Iterator function to sort Customers by name
    """
    return customer.name


def getVehicleType(customer):
    """
    Iterator function to sort Customers by Vehicle type
    """
    return customer.vehicle_type


def parse_line(line: str) -> List[str]:
    """
    Check separation character and split line into a list

    Note: this is perhaps too lenient depending on the requirements. For example
      with this logic, it is possible to have a file with both comma-separated
      and pipe-separated data in the same file. And maybe that's ok.

    """

    if "|" in line:
        pipe_separated_data = [x.strip() for x in line.split(r'|')]
        return pipe_separated_data
    elif "," in line:   
        comma_separated_data = [x.strip() for x in line.split(r',')]
        return comma_separated_data
    else:
        return None



def parse_file(filepath: str, sorted: str = None) -> Iterable[Customer]:
    """
    Parse text at given filepath and sort if needed

    """
    
    # Validation
    if type(filepath) is not str:
        return 'Filepath must be a string'

    if not os.path.exists(filepath):
        return 'File {} does not exist'.format(filepath)

    
    customers = []
    
    # open the file and read through it line by line
    with open(filepath, 'r') as file_object:

        for line in file_object:
            row = parse_line(line)

            if row:
                # Assumes consistent order of data in files 
                # (ex: first two values are always first/last name)
                c = Customer("{} {}".format(row[0], row[1]), row[2], row[3], row[4], row[5])
                customers.append(c)

    # Check for sort options
    if sorted is 'name':
        customers.sort(key=getName)

    elif sorted is 'vehicle_type':
        customers.sort(key=getVehicleType)


    return customers




if __name__ == "__main__":
    """
    CLI Module to import and list Outdoor.sy customers
    * Display the information Outdoor.sy wants to see about their customers
    * Optionally sort the data by Vehicle type or by Full name

    """

    filepath = ''
    sort = None

    # If no args passed, assume human-triggered
    if len(sys.argv) == 1:
        questions = [
            inquirer.Path("filepath", message="Which file would you like to import and list?", exists=True, normalize_to_absolute_path=True, path_type=inquirer.Path.FILE),
            inquirer.List("sort", message="Would you like to sort the data in {filepath}?", choices=['No thanks', 'name', 'vehicle_type'])
        ]

        answers = inquirer.prompt(questions)

        if answers["sort"] is "No thanks":
            sort = None
        else:
            sort = answers["sort"]

        filepath = answers["filepath"]


    # This else block will cover --help and automated usage
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "file",
            type=argparse.FileType('r'), # This includes builtin filepath validation
            help="filepath to Customer data you would like to list")
        parser.add_argument(
            '--sort',
            default=None,
            help="sort customers by name or vehicle_type (defaults to None)")


        args = parser.parse_args()
        args.file.close() # Close TextIOWrapper

        filepath = args.file.name
        sort = args.sort


    customers = parse_file(filepath, sort)

    print('Import successful! Printing customer output...\n\n{}'.format(customers))

