#!/usr/bin/python

import csv
import os
import re


data_folder = 'data'
prices = [
    'houses_2009',
    'houses_2010',
    'houses_2011',
    'houses_2012',
    'houses_2013',
]

districte_re = re.compile(r'(^\d+)\.')
data = []
new_row = {}
cols = []
for price_id in prices:
    filename = os.path.join(data_folder, price_id + '.csv')
    cols.append(price_id)
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            districte = re.findall(districte_re, row[1])
            if len(districte) != 1:
                # Skip first and empty lines.
                continue
            districte = districte[0]
            if districte not in new_row:
                new_row[districte] = []
            new_row[districte].append(row[2])

cadastrals = [
    'cadastral_2011',
    'cadastral_2012',
    'cadastral_2013',
    'cadastral_2014',
]

for cadastral in cadastrals:
    filename = os.path.join(data_folder, cadastral + '.csv')
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for line_number, row in enumerate(reader):
            if line_number == 0:
                for name in row:
                    if not name:
                        break
                    cols.append(name)
            districte = re.findall(districte_re, row[1])
            if len(districte) != 1:
                # Skip first and empty lines.
                continue
            districte = districte[0]
            


print 'cols', cols

