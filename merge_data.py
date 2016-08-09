"""Prepares a full set of data for Barcelona housing price prediction.

The resulting data is a composite set of features.
"""

import csv
import os
import re
import sys

from third_party import gflags

gflags.DEFINE_string('output', '',
                     'Path to the output csv.')
gflags.DEFINE_string('data_folder', 'data',
                     'Path to the folder with data files.')
FLAGS = gflags.FLAGS


def main(argv):
    argv = FLAGS(argv)
    prices = [
        'houses_2009',
        'houses_2010',
        'houses_2011',
        'houses_2012',
        'houses_2013',
    ]

    districte_re = re.compile(r'(^\d+)\.')
    # A dictionary indexed by districte that contains a list of feature values.
    new_rows = {}
    # The name of the features.
    cols = []

    # First the new_rows is initialized with the key (i.e. districte).
    for price_id in prices:
        filename = os.path.join(FLAGS.data_folder, price_id + '.csv')
        cols.append(price_id)
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                districte = re.findall(districte_re, row[1])
                if len(districte) != 1:
                    # Skip first and empty lines.
                    continue
                districte = districte[0]
                if districte not in new_rows:
                    new_rows[districte] = []
                new_rows[districte].append(row[2])

    # Next, new features are added for each "districte".
    cadastrals = [
        'cadastral_2011',
        'cadastral_2012',
        'cadastral_2013',
        'cadastral_2014',
    ]

    for cadastral in cadastrals:
        filename = os.path.join(FLAGS.data_folder, cadastral + '.csv')
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
                if districte not in new_rows:
                    raise Exception('Districte key "%s" not in new_rows' %
                                    districte)
                for value in row[2:]:
                    if not value:
                        break
                    new_rows[districte].append(value)

    print 'cols:', cols
    print 'Districtes:', new_rows.keys()

    # Save final csv.
    with open(FLAGS.output, 'w') as f:
        line = ';'.join(cols)
        f.write(line + '\n')
        for districte, values in new_rows.iteritems():
            line = '%s;%s' % (districte, ';'.join(values))
            f.write(line + '\n')


if __name__ == '__main__':
    main(sys.argv)
