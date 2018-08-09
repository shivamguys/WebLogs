#!/usr/bin/python
from sys import *;
def f():
	oldvalue=None;
	maxsales=[0.0];
	for i in stdin:
		i=i.strip().split("\t");
		#print(i)
		if(len(i)!=2):
			continue;

		currentstore,sales=i[0],i[1];
		if(oldvalue and oldvalue!=currentstore):
			print("{0}\t{1}".format(oldvalue,maxsales[0]));
			
			maxsales[0]=0.0
		if(float(sales)>maxsales[0]):
			#print("true");
			#global  maxsales;			
			maxsales[0]=float(sales);
		oldvalue=currentstore;
	if oldvalue:
		print("{0}\t{1}".format(oldvalue,maxsales[0]));



f()
