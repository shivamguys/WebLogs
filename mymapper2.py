#!/usr/bin/python
from sys import *;
oldstore=None
#First value is count and second is sales
desc=[0,0.0];
count=1;
for i in stdin:
	i=i.strip().split("\t");
	if(len(i)>=5):
		print("{0}\t{1}\t{2}".format(i[2].strip(),count,i[4].strip()))
