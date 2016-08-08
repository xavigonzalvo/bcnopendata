#!/usr/bin/python

import urllib2
import os

HOUSING_CSV_2009 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2009_HABITATGES_2NA_MA.csv&name=opendata_2009_HABITATGES_2NA_MA.csv'
HOUSING_CSV_2010 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2010_HABITATGES_2NA_MA.csv&name=opendata_2010_HABITATGES_2NA_MA.csv'
HOUSING_CSV_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2011_HABITATGES_2NA_MA.csv&name=opendata_2011_HABITATGES_2NA_MA.csv'
HOUSING_CSV_2012 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2012_HABITATGES_2NA_MA.csv&name=opendata_2012_HABITATGES_2NA_MA.csv'
HOUSING_CSV_2013 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2013_HABITATGES_2NA_MA.csv&name=opendata_2013_HABITATGES_2NA_MA.csv'
HOUSING_2007_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2fh2maveanualt1b.csv&name=h2maveanualt1b.csv'

CADASTRAL_2009 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2flocalsval2009.csv&name=localsval2009.csv'
CADASTRAL_2010 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2flocalsval2010.csv&name=localsval2010.csv'
CADASTRAL_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2011_localsval2011.csv&name=localsval2011.csv'
CADASTRAL_2012 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2012_localsval2012.csv&name=localsval2012.csv'
CADASTRAL_2013 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2013_localsval2013.csv&name=localsval2013.csv'
CADASTRAL_2014 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2014_localsval2014.csv&name=localsval2014.csv'

FAMILY_HOUSING_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2011_HABIT_FAM_SIT_EDIF_DEST_HABIT_SEGONS_TIP2011.csv&name=HABIT_FAM_SIT_EDIF_DEST_HABIT_SEGONS_TIP2011.csv'
FAMILY_HOUSING_PER_YEAR_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2011_HABIT_FAM_DEST_HABIT_SEGONS_ANY_CONST2011.csv&name=HABIT_FAM_DEST_HABIT_SEGONS_ANY_CONST2011.csv'

HEATING_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2011_HABIT_PPAL_SEGONS_INSTAL1_CALEF2011.csv&name=HABIT_PPAL_SEGONS_INSTAL1_CALEF2011.csv'

PEOPLE_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2011_HABIT_PPAL_SEGONS_NOMBRE_PERS_VIUEN2011.csv&name=HABIT_PPAL_SEGONS_NOMBRE_PERS_VIUEN2011.csv'

ROOMS_2011 = 'http://opendata.bcn.cat/opendata/en/descarrega-fitxer?url=http%3a%2f%2fbismartopendata.blob.core.windows.net%2fopendata%2fopendata%2f2011_HABIT_PPAL_SEGONS_NOM_HABIT2011.csv&name=HABIT_PPAL_SEGONS_NOM_HABIT2011.csv'

housing_data = {
    'houses_2009': HOUSING_CSV_2009,
    'houses_2010': HOUSING_CSV_2010,
    'houses_2011': HOUSING_CSV_2011,
    'houses_2012': HOUSING_CSV_2012,
    'houses_2013': HOUSING_CSV_2013,
    'houses_2007_2011': HOUSING_2007_2011,
    'cadastral_2009': CADASTRAL_2009,
    'cadastral_2010': CADASTRAL_2010,
    'cadastral_2011': CADASTRAL_2011,
    'cadastral_2012': CADASTRAL_2012,
    'cadastral_2013': CADASTRAL_2013,
    'cadastral_2014': CADASTRAL_2014,
    'family_housing_2011': FAMILY_HOUSING_2011,
    'family_housing_peryear_2011': FAMILY_HOUSING_PER_YEAR_2011,
    'heating_2011': HEATING_2011,
    'people_2011': PEOPLE_2011,
    'rooms_2011': ROOMS_2011,
}

data_folder = 'data/'

if not os.path.isdir(data_folder):
    os.makedirs(data_folder)

for name, url in housing_data.items():
    filename = os.path.join(data_folder, name) + '.csv'
    if os.path.exists(filename):
        continue
    print 'Downloading', filename
    try:
        downloaded_data  = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print 'Error for %s: %s' % (name, e)
        continue
    with open(filename, 'w') as f:
        f.write(downloaded_data.read())
