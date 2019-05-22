#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2018 University of Virginia. All rights reserved.

file      test.py
author    Yuanlong Tan <yt4xb@virginia.edu>
version   1.0
date      Oct. 1, 2018
brief     add timestamp for rtstats.log.
usage     python test.py <log> <logfile-to-write>
"""

from __future__ import division
import csv
import re
import sys
#import pytz
import subprocess
#from dateutil.parser import parse
from datetime import datetime, timedelta


def parseMLDM(feedtype, line):
	"""Parses the product size and elapsed time received by MLDM.

	Parses the product size and elapsed receiving time consumed
	for the product (which is received by MLDM) in the given line
	of log file.

	Args:
		line: A line of the raw log file.

	Returns:
		(-1, -1, -1): If no valid size or time is found.
		(prodindex, prodsize, rxtime): A tuple of product index, product size
									   and receiving time.
	"""
	match =	re.search(r'.*' + feedtype, line)
	if match:
		match = re.search(r'.*mldm.*Received', line)
		if match:
			split_line = line.split()
			arrival_time = datetime.strptime(split_line[0], "%Y%m%dT%H%M%S.%fZ")
			insert_time  = datetime.strptime(split_line[7], "%Y%m%d%H%M%S.%f")
			# the last column is product index
            		prodindex = int(split_line[9])
			# col 6 is size in bytes
			size = int(split_line[6])
			# col 0 is the arrival time, col 7 is the insertion time.
			# arrival_time = parse(split_line[0]).astimezone(pytz.utc).arrival_time.replace(tzinfo=None)
			rxtime = (arrival_time - insert_time).total_seconds()
			return (prodindex, size, rxtime)
		else:
			return (-1, -1, -1)
	else:
		return (-1, -1, -1)


def parseBackstop(feedtype, line):
	"""Parses the product size and elapsed time received by the backstop.

	Parses the product size and elapsed receiving time consumed for the
	product (which is received by the backstop) in the given line of log file.

	Args:
		line: A line of the raw log file.

	Returns:
		(-1, -1, -1): If no valid size or time is found.
		(prodindex, prodsize, rxtime): A tuple of product index, product size
									   and receiving time.
	"""
    	match = re.search(r'.*' + feedtype, line)
    	if match:
        	match = re.search(r'.*down7.*Inserted', line)
        	if match:
			split_line = line.split()
			arrival_time = datetime.strptime(split_line[0], "%Y%m%dT%H%M%S.%fZ")
			insert_time  = datetime.strptime(split_line[6], "%Y%m%d%H%M%S.%f")
			# the last column is product index
			prodindex = int(split_line[8])
			# col 6 is size in bytes
			size = int(split_line[5])
			# col 0 is the arrival time, col 7 is the insertion time.
			# arrival_time = parse(split_line[0]).astimezone(pytz.utc).arrival_time.replace(tzinfo=None)
			rxtime = (arrival_time - insert_time).total_seconds()
			return (prodindex, size, rxtime)
   		else:
    			return (-1, -1, -1)
	else:
		return (-1, -1, -1)

def extractLog(feedtype, filename):
	"""Extracts the key information from the log file.

	Args:
		filename: Filename of the log file.

	Returns:
		(complete_set, complete_dict, vset, vset_dict): extracted groups.
	"""
	complete_set  = set()
	complete_dict = {}
	# vset contains the products received by VCMTP
	vset = set()
	vset_dict = {}
	with open(filename, 'r') as logfile:
		for i, line in enumerate(logfile):
			(mprodid, msize, mrxtime) = parseMLDM(feedtype, line)
			(bprodid, bsize, brxtime) = parseBackstop(feedtype, line)
			if mprodid >= 0:
				complete_set |= {mprodid}
				vset |= {mprodid}
				if not complete_dict.has_key(mprodid):
					complete_dict[mprodid] = (msize, mrxtime)
					vset_dict [mprodid]= (msize, mrxtime)
			elif bprodid >= 0:
				complete_set |= {bprodid}
				if not complete_dict.has_key(bprodid):
					complete_dict[bprodid] = (bsize, brxtime)
	logfile.close()
	return (complete_set, complete_dict, vset, vset_dict)

def aggThru(complete_set, complete_dict, vset, vset_dict):
	"""Aggregate for calculating throughput.

	Args:
		complete_set: Set of complete products.
		complete_dict: Dict of complete products.
		vset:
		vset_dict:

	Returns:
		(complete_size, complete_time, ffdr_size, ffdr_time): metrics for calculating throughputs.
	"""
	complete_size = 0
	complete_time = 0
	for i in complete_set:
		complete_size += complete_dict[i][0]
		complete_time += complete_dict[i][1]
	ffdr_size = 0
	ffdr_time = 0
	for i in vset:
		ffdr_size += vset_dict[i][0]
		ffdr_time += vset_dict[i][1]
	return (complete_size, complete_time, ffdr_size, ffdr_time)



def main(logfile, csvfile):
	"""Reads the raw log file and parses it.

	Reads the raw ldmd log file, parses each line and computes throughput
	and VSR over an aggregate size.

	Args:
		logfile: Filename of the log file.
		csvfile : Filename of the new file to contain output results.
	"""
    local_time = "201901064201Z"
    time = datetime.strptime(time, "%Y%m%dT%H%M%SZ")
	w = open(csvfile, 'w+')
	   with open(logfile, 'r') as logfile:
           for i, line in enumerate(logfile):
               string = str(time) + ',' + line
               w.write(string)
               time = time + timedelta(seconds=1)
       logfile.close()

	w.close()


if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])
