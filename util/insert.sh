#!/bin/bash

# recommend sleeping for 30*number of receivers
# because the initialization is sequential
sleep 40
pq_test_insert -f NGRID -v /home/ldm7/LDM6-LDM7-comparison/std_data/1hr_NGRID.txt
