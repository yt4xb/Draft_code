#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2018 University of Virginia. All rights reserved.

file      LDM7_deploy.sh
author    Yuanlong Tan <yt4xb@virginia.edu>
version   1.0
date      Oct. 22, 2018

LICENSE
This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2 of the License, or（at your option）
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details at http://www.gnu.org/copyleft/gpl.html

brief     Script for installing LDM7
"""
sudo yum install -y libxml2-devel
sudo yum install -y libpng-devel
sudo yum install -y zlib1g-devel
sudo yum install -y pax
sudo yum install -y libyaml-devel
sudo yum install -y gcc
sudo yum install -y g++
sudo yum install -y ntp
sudo yum install -y autoconf
sudo yum install -y m4
sudo yum install -y automake make
sudo yum install -y gnuplot
gunzip -c ldm-6.13.6.tar.gz | pax -r '-s:/:/src/:'
cd ldm-6.13.6/src
./configure --with-debug --with-multicast --disable-root-actions CFLAGS=-o0 -g CXXFLAGS=-o0 -g -std=c++11 >configure.log 2>&1
make install >make.log 2>&1
sudo make root-actions
