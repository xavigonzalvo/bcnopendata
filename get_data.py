#!/usr/bin/python

import urllib2
import os

HOUSING_CSV_2009 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2009_HABITATGES_2NA_MA.csv&name=opendata_2009_HABITATGES_2NA_MA.csv'
HOUSING_CSV_2010 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2010_HABITATGES_2NA_MA.csv&name=opendata_2010_HABITATGES_2NA_MA.csv'
HOUSING_CSV_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2011_HABITATGES_2NA_MA.csv&name=opendata_2011_HABITATGES_2NA_MA.csv'
HOUSING_CSV_2012 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2012_HABITATGES_2NA_MA.csv&name=opendata_2012_HABITATGES_2NA_MA.csv'
HOUSING_CSV_2013 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2013_HABITATGES_2NA_MA.csv&name=opendata_2013_HABITATGES_2NA_MA.csv'

housing_data = {
    'houses_2009': HOUSING_CSV_2009,
    'houses_2010': HOUSING_CSV_2010,
    'houses_2011': HOUSING_CSV_2011,
    'houses_2012': HOUSING_CSV_2012,
    'houses_2013': HOUSING_CSV_2013,
}

data_folder = 'data/'

if not os.path.isdir(data_folder):
    os.makedirs(data_folder)

for name, url in housing_data.items():
    downloaded_data  = urllib2.urlopen(url)
    filename = os.path.join(data_folder, name) + '.csv'
    if os.path.exists(filename):
        continue
    print 'Downloading', filename
    with open(filename, 'w') as f:
        f.write(downloaded_data.read())
