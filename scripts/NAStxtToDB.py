# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:40:48 2017

@author: SERNMO
"""
# Import packages and libraries
import datetime
import glob
import re
import connection

# Search for files and paths for current date
root = '/mnt/nas/CMS_Data'
year = datetime.date.today().strftime("%Y")
month = datetime.date.today().strftime("%Y-%m")
day = datetime.date.today().strftime("%Y-%m-%d")
files = glob.glob("%s/StationsData_*/*/Converted to TXT/%s/%s/*%s.txt" % (root, year, month, day))
load_sql = ("LOAD DATA LOCAL INFILE '%s' "
            "INTO TABLE %s " 
            "FIELDS TERMINATED BY '\t' " 
            "LINES TERMINATED BY '\n' "
            "IGNORE 1 LINES; ")

# Load text files to MySQL DB
connection = connection.getConnection()
cursor = connection.cursor()
for file in files:
    print(file)
    station = re.findall('\[([0-9]+)\]', file)[0]
    table = 'SIN' + station
    print(table)
    cursor.execute(load_sql % (file, table))    
    connection.commit()
connection.close()
