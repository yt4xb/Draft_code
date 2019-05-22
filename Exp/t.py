import csv
import re
import sys
import numpy as np
Thru = []
filename = sys.argv[1]
with open(filename, 'r') as logfile:
        for i, line in enumerate(logfile):
		match = re.search(r'\d+', line)
		if match:
			split_line = line.split(',')
			thru = float(split_line[4])
			if thru != 0:
				Thru.append(thru)
#min_thru = np.min(Thru)
#max_thru = np.max(Thru)
mean_thru = np.mean(Thru)
#median_thru = np.median(Thru)
#qthru = np.percentile(Thru,25)
#tqthru = np.percentile(Thru,75)
#print str(min_thru) + ',' + str(qthru) + ',' + str(median_thru) + ',' \
#	+ str(tqthru) + ',' + str(max_thru) + ',' + str(mean_thru)
print str(mean_thru)
