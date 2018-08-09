#!/usr/bin/python
from sys import *
oldsales=None;
totalsales=[0.0]
for i in stdin:
	i=i.strip().split("\t");
		
	#if((i[0].strip()=="Consumer Electronics")or(i[0].strip()=="Toys")):
	if(i[0].strip()=="Consumer Electronics" or i[0].strip()=="Toys"):	
	
		#print(i[0].strip());
		current=i[0];
		currentcost=i[1];
		if(oldsales and oldsales!=current):
			#global totalsales
			print("{0}\t{1}".format(oldsales,totalsales[0]));
			totalsales[0]=0.0;
		#global totalsales
		oldsales=current;
		totalsales[0]=float(currentcost)+totalsales[0];
	else:
		continue;
	

if oldsales:
	print("{0}\t{1}".format(oldsales,totalsales[0]));
