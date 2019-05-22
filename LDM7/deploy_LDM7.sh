# -*- coding: utf-8 -*-

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
