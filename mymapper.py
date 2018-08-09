#!/usr/bin/python
import sys;
for i in sys.stdin:
	i=i.strip().split("\t");
	if(len(i)!=6):
		continue;
	product=i[3].strip();
	cost=i[4];
	#if(product=="Consumer Electronics" or product=="Toys"):
	if(product=="Consumer Electronics" or product=="Toys"):
		print("{0}\t{1}".format(product,cost));

