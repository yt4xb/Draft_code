#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2018 University of Virginia. All rights reserved.

file      std_process.py
author    Yuanlong Tan <yt4xb@virginia.edu>
version   1.0
date      Jan. 10, 2019
brief     Process std data.
usage     python std_process.py <std_data> <1h_std_data-to-write>
"""

from __future__ import division
import csv
import re
import sys
#import pytz
import subprocess
#from dateutil.parser import parse
from datetime import datetime, timedelta


def parse(start_time, end_time, line):
    split_line = line.split()
    time = datetime.strptime(split_line[1], "%Y%m%d%H%M%S.%f")
    if time > start_time: 
	if time < end_time:
    		size = int(split_line[0])
    		return (size, time)
	else: 
		return (-1, -1)
    else: 
	return (-1, -1)

def main(logfile, csvfile):

    start_time = datetime.strptime("20181114130000.000000", "%Y%m%d%H%M%S.%f")
    end_time = datetime.strptime("20181114140000.000000", "%Y%m%d%H%M%S.%f")
    w = open(csvfile, 'w+')
    with open(logfile, 'r') as r:
    	for i, line in enumerate(r):
        	(size, time) = parse(start_time, end_time, line)
       		if size > 0:
			tmp_str = str(time) + ',' + str(complete_size) + '\n'
        		w.write(tmp_str)
    r.close()
    w.close()

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])
