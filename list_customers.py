#!/usr/bin/env python

import inquirer
import csv


class Customer:
    def __init__(self, name, email, vehicle_type, vehicle_name, vehicle_length):
        self.name = name
        self.email = email
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.vehicle_length = vehicle_length

    def __repr__(self):
        return f'Customer({self.name!r}, {self.email!r}, {self.vehicle_type!r}, {self.vehicle_name!r}, {self.vehicle_length!r})'



def read_customers_from_file(filename):
    customers = []
    with open(filename, "r") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            c = Customer("{} {}".format(row[0], row[1]), row[2], row[3], row[4], row[5])
            customers.append(c)
    
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


    customers = read_customers('tests/commas.txt')

    print(customers)

