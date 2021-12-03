import os
import csv


def write_csv_file(fname, data, *args, **kwargs):
    """
    @param fname: string, name of file to write
    @param data: list of list of items

    Write data to file
    """
    csv_file = csv.writer(open(fname, 'w'), *args, **kwargs)

    for row in data:
        csv_file.writerow(row)
