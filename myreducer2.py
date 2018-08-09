#!/usr/bin/python
from sys import *;

desc=[0,0.0]
for i in stdin:
	i=i.strip().split("\t");
	if(len(i)>=3): 
		store,count,sales=i[0],i[1],i[2];
		desc[0]=desc[0]+1;
		desc[1]=desc[1]+float(sales);
print("{0}\t{1}".format(desc[0],desc[1]));
