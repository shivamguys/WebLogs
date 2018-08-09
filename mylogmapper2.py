#!/usr/bin/python
from sys import *;
for i in stdin:
	i=i.strip().split(" ");
# i will be passing only this ip adress to reduce the overhead
	if(i[0]=="10.99.99.186"):
		print("{0}".format(i[0]));
