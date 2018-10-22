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
sudo apt-get install -y libxml2-dev
sudo apt-get install -y libpng-dev
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y pax
sudo apt-get install -y libyaml-dev
sudo apt-get install -y gcc
sudo apt-get install -y g++
sudo apt-get install -y ntp
sudo apt-get install -y autoconf
sudo apt-get install -y m4
sudo apt-get install -y automake make
sudo apt-get install -y gnuplot
gunzip -c ldm-6.13.6.tar.gz | pax -r '-s:/:/src/:'
cd ldm-6.13.6/src

#./configure --with-debug --with-multicast --disable-root-actions CFLAGS='-o0 -g' CXXFLAGS='-o0 -g -std=c++11' &>configure.log && echo Configured
#make install &> make.log && echo Installed
#sudo make root-actions
