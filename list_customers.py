#!/usr/bin/env python

from typing import List, Iterable

import inquirer
import os


class Customer:
    def __init__(self, name, email, vehicle_type, vehicle_name, vehicle_length):
        self.name = name
        self.email = email
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.vehicle_length = vehicle_length

    def __repr__(self):
        return f'Customer({self.name!r}, {self.email!r}, {self.vehicle_type!r}, {self.vehicle_name!r}, {self.vehicle_length!r})'


def getName(obj):
    return obj.name


def getVehicleType(obj):
    return obj.vehicle_type


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
    Parse text at given filepath

    """
    
    # Validation
    if type(filepath) is not str:
        return 'Filepath must be a string'

    if not os.path.exists(filepath):
        return 'File does not exist'

    
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
    CLI Module to list Outdoor.sy customers
    * Display the information Outdoor.sy wants to see about their customers
    * Sort the data by Vehicle type or by Full name
    """

    """
    Arg ideas:
    *  file_path (will also include a file dialog  using tkinter)
    *  to_file: log results to a file (using the logger init above)

    Implementation:
    * Parses the file (via comma or pipe) and saves the data to a list of Customer objects
        customers = [ {Customer},  {Customer}, {Customer}, ... ]
              
    * ?

    """

    customers = parse_file('tests/commas.txt')

    print(customers)

