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

import urllib2
import urllib
import sys
import time
import string
import json
import yaml
global values1
values1 = {}

def readAccount(filename):
	f = open(filename, 'r+')
	jsonData = yaml.load(f)
	username = jsonData['username']
	passwd = jsonData['passwd']
	gh_url = 'https://al2s.net.internet2.edu/oess-service-basic/data.cgi'
	values1 = {'method' : 'get_workgroups'}
	data1 = urllib.urlencode(values1, doseq=True)
	req1 = urllib2.Request(gh_url, data1)
	password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_manager.add_password(None, gh_url, username, passwd)
	auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
	opener = urllib2.build_opener(auth_manager)
	urllib2.install_opener(opener)
	handler1 = urllib2.urlopen(req1)
	result1 = handler1.read()
	jsonData1 = json.loads(result1)
	return jsonData1


