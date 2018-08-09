#!/usr/bin/python
import sys;
for i in sys.stdin:
	i=i.strip().split("\t");
	if(len(i)==6):
		store=i[2].strip();
		sale=i[4].strip();
		print("{0}\t{1}".format(store,sale));

