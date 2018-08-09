#!/usr/bin/python
from sys import *;
a=None
for i in stdin:
	i=i.strip().split(" ");
	#print("{0}".format(len(i)));
	#i=i.split("");
	s=i[6].strip('"'); #this is the working phase
	#if(i[1]=="-"):
	#	print("Yes this is empty");
	if(s=="/assets/js/the-associates.js"):	
		print("{0}".format(s));
	else:
		continue;

