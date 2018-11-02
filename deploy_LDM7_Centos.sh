# -*- coding: utf-8 -*-

sudo yum install -y libxml2-devel
sudo yum install -y libpng-devel
sudo yum install -y zlib1g-devel
sudo yum install -y pax
sudo yum install -y libyaml-devel
sudo yum install -y gcc
sudo yum install -y gcc-c++
sudo yum install -y ntp
sudo yum install -y autoconf
sudo yum install -y m4
sudo yum install -y automake make
sudo yum install -y gnuplot
gunzip -c ldm-6.13.6.tar.gz | pax -r '-s:/:/src/:'
cd ldm-6.13.6/src

#./configure --with-debug --with-multicast --disable-root-actions CFLAGS='-o0 -g' CXXFLAGS='-o0 -g -std=c++11' &>configure.log && echo Configured
#make install &> make.log && echo Installed
#sudo make root-actions
