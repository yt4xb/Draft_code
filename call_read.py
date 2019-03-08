#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2018 University of Virginia. All rights reserved.

file      read_test.py
author    Yuanlong Tan <yt4xb@virginia.edu>
version   1.0
date      Feb. 14, 2019
brief     
"""

import read_test
import sys

jsonfile = sys.argv[1]
results = read_test.readAccount(jsonfile)

print results

