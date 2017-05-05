# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:40:48 2017

@author: SERNMO
"""
# Import packages and libraries
import datetime

# Search for files and paths for current date
root = '/mnt/nas/CMS_Data'
year = datetime.date.today().strftime("%Y")
month = datetime.date.today().strftime("%Y-%m")
day = datetime.date.today().strftime("%Y-%m-%d")
