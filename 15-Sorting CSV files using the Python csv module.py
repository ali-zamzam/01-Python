"""Sorting CSV files using the Python csv module

I wanted to summarize a way to sort CSV files by just using the csv module and other standard library Python modules
(you probably also want to consider using the pandas library if you are working with very large CSV files - I am planning to make this a separate topic).

"""


# Sections
# Reading in a CSV file
# Printing the CSV file contents
# Converting numeric cells to floats
# Sorting the CSV file
# Marking min/max values in particular columns
# Writing out the modified table to as a new CSV file
# Batch processing CSV files


# Objective:
# Let us assume that we have an example CSV file formatted like this:

# name,column1,column2,column3
# abc,1.1,4.2,1.2
# def,2.1,1.4,5.2
# ghi,1.5,1.2,2.1
# jkl,1.8,1.1,4.2
# mno,9.4,6.6,6.2
# pqr,1.4,8.3,8.4
# And we want to sort particular columns and eventually mark min- of max-values in the table.




"""Reading in a CSV file"""
# Because we will be iterating over our CSV file a couple of times, let us read in the CSV file using the csv module and hold the contents in memory using a Python list object (note: be careful with very large CSV files and possible memory issues associated with this approach).

import csv


def csv_to_list(csv_file, delimiter=','):
    """ 
    Reads in a CSV file and returns the contents as list,
    where every row is stored as a sublist, and each element
    in the sublist represents 1 cell in the table.
    
    """
    with open(csv_file, 'r') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)
csv_cont = csv_to_list('../Data/test.csv')

print('first 3 rows:')
for row in range(3):
    print(csv_cont[row])
# first 3 rows:
# ['name', 'column1', 'column2', 'column3']
# ['abc', '1.1', '4.2', '1.2']
# ['def', '2.1', '1.4', '5.2']



"""Printing the CSV file contents""""


# Also, let us define a short function that prints out the CSV file to the standard output
#  screen in a slightly prettier format:

def print_csv(csv_content):
    """ Prints CSV file to standard output."""
    print(50*'-')
    for row in csv_content:
        row = [str(e) for e in row]
        print('\t'.join(row))
    print(50*'-')
csv_cont = csv_to_list('../Data/test.csv')

print('\n\nOriginal CSV file:')
print_csv(csv_cont)
# Original CSV file:
# --------------------------------------------------
# name	column1	column2	column3
# abc	1.1	4.2	1.2
# def	2.1	1.4	5.2
# ghi	1.5	1.2	-2.1
# jkl	1.8	-1.1	4.2
# mno	9.4	6.6	6.2
# pqr	1.4	8.3	8.4
# --------------------------------------------------



"""Converting numeric cells to floats"""
# To avoid problems with the sorting approach that can occur when we have negative values in some cells, 
# let us define a function that converts all numeric cells into float values.

def convert_cells_to_floats(csv_cont):
    """ 
    Converts cells to floats if possible
    (modifies input CSV content list).
    
    """
    for row in range(len(csv_cont)):
        for cell in range(len(csv_cont[row])):
            try:
                csv_cont[row][cell] = float(csv_cont[row][cell])
            except ValueError:
                pass 
print('first 3 rows:')
for row in range(3):
    print(csv_cont[row])
# first 3 rows:
# ['name', 'column1', 'column2', 'column3']
# ['abc', '1.1', '4.2', '1.2']
# ['def', '2.1', '1.4', '5.2']



"""Sorting the CSV file"""


# Using the very handy operator.itemgetter function, we define a function that returns a CSV file 
# contents sorted by a particular column (column index or column name).


import operator


def sort_by_column(csv_cont, col, reverse=False):
    """ 
    Sorts CSV contents by column name (if col argument is type <str>) 
    or column index (if col argument is type <int>). 
    
    """
    header = csv_cont[0]
    body = csv_cont[1:]
    if isinstance(col, str):  
        col_index = header.index(col)
    else:
        col_index = col
    body = sorted(body, 
           key=operator.itemgetter(col_index), 
           reverse=reverse)
    body.insert(0, header)
    return body
# To see how (and if) it works, let us sort the CSV file in ../Data/test.csv by the column name "column3".

csv_cont = csv_to_list('../Data/test.csv')

print('\n\nOriginal CSV file:')
print_csv(csv_cont)

print('\n\nCSV sorted by column "column3":')
convert_cells_to_floats(csv_cont)
csv_sorted = sort_by_column(csv_cont, 'column3')
print_csv(csv_sorted)
# Original CSV file:
# --------------------------------------------------
# name	column1	column2	column3
# abc	1.1	4.2	1.2
# def	2.1	1.4	5.2
# ghi	1.5	1.2	-2.1
# jkl	1.8	-1.1	4.2
# mno	9.4	6.6	6.2
# pqr	1.4	8.3	8.4
# --------------------------------------------------


# CSV sorted by column "column3":
# --------------------------------------------------
# name	column1	column2	column3
# ghi	1.5	1.2	-2.1
# abc	1.1	4.2	1.2
# jkl	1.8	-1.1	4.2
# def	2.1	1.4	5.2
# mno	9.4	6.6	6.2
# pqr	1.4	8.3	8.4
# --------------------------------------------------






"""Marking min/max values in particular columns"""


# To visualize minimum and maximum values in certain columns if find it quite useful to add 
# little symbols to the cells (most people like to highlight cells with colors in e.g., 
# Excel spreadsheets, but CSV doesn't support colors, so this is my workaround - 
# please let me know if you figured out a better approach, I would be looking forward to your suggestion).

def mark_minmax(csv_cont, col, mark_max=True, marker='*'):
    """
    Sorts a list of CSV contents by a particular column 
    (see sort_by_column function).
    Puts a marker on the maximum value if mark_max=True,
    or puts a marker on the minimum value mark_max=False
    (modifies input CSV content list).
    
    """
    
    sorted_csv = sort_by_column(csv_cont, col, reverse=mark_max)
    if isinstance(col, str):  
        col_index = sorted_csv[0].index(col)
    else:
        col_index = col
    sorted_csv[1][col_index] = str(sorted_csv[1][col_index]) + marker
    return None


def mark_all_col(csv_cont, mark_max=True, marker='*'):
    """
    Marks all maximum (if mark_max=True) or minimum (if mark_max=False)
    values in all columns of a CSV contents list - except the first column.
    Returns a new list that is sorted by the names in the first column
    (modifies input CSV content list).
    
    """
    for c in range(1, len(csv_cont[0])):
        mark_minmax(csv_cont, c, mark_max, marker)
    marked_csv = sort_by_column(csv_cont, 0, False)
    return marked_csv
import copy

csv_cont = csv_to_list('../Data/test.csv')

csv_marked = copy.deepcopy(csv_cont)
convert_cells_to_floats(csv_marked)
mark_all_col(csv_marked, mark_max=False, marker='*')
print_csv(csv_marked)
print('*: min-value')
# --------------------------------------------------
# name	column1	column2	column3
# abc	1.1*	4.2	1.2
# def	2.1	1.4	5.2
# ghi	1.5	1.2	-2.1*
# jkl	1.8	-1.1*	4.2
# mno	9.4	6.6	6.2
# pqr	1.4	8.3	8.4
# --------------------------------------------------
# *: min-value



"""Writing out the modified table to as a new CSV file"""


# After the sorting and maybe marking of minimum and maximum values, we likely want to write out 
# the modified data table as CSV file again.

def write_csv(dest, csv_cont):
    """ Writes a comma-delimited CSV file. """

    with open(dest, 'w') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        for row in csv_cont:
            writer.writerow(row)

write_csv('../Data/test_marked.csv', csv_marked)
# Let us read in the written CSV file to confirm that the formatting is correct:

csv_cont = csv_to_list('../Data/test_marked.csv')

print('\n\nWritten CSV file:')
print_csv(csv_cont)
# Written CSV file:
# --------------------------------------------------
# name	column1	column2	column3
# abc	1.1*	4.2	1.2
# def	2.1	1.4	5.2
# ghi	1.5	1.2	-2.1*
# jkl	1.8	-1.1*	4.2
# mno	9.4	6.6	6.2
# pqr	1.4	8.3	8.4
# --------------------------------------------------



"""Batch processing CSV files"""


# Usually, CSV files never come alone, but we have to process a whole bunch of similar formatted CSV files from 
# some output device.
# For example, if we want to process all CSV files in a particular input directory and want 
# to save the processed files in a separate output directory, we can use a simple list comprehension 
# to collect tuples of input-output file names.

import os

in_dir = 'data'
out_dir = '../Data/processed'
csvs = [
    (os.path.join(in_dir, csv), 
        os.path.join(out_dir, csv))
    for csv in os.listdir(in_dir) 
    if csv.endswith('.csv')
    ]

for i in csvs:
    print(i)
('../Data/test.csv', '../Data/processed/test.csv')
('../Data/test_marked.csv', '../Data/processed/test_marked.csv')

# Next, we can summarize the processes we want to apply to the CSV files in a simple function and loop over our file names:

def process_csv(csv_in, csv_out):
    """ 
    Takes an input- and output-filename of an CSV file
    and marks minimum values for every column.
    
    """
    csv_cont = csv_to_list(csv_in)
    csv_marked = copy.deepcopy(csv_cont)
    convert_cells_to_floats(csv_marked)
    mark_all_col(csv_marked, mark_max=False, marker='*')
    write_csv(csv_out, csv_marked)
for inout in csvs:
    process_csv(inout[0], inout[1])
