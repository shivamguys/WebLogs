#!/usr/bin/python
from sys import *
ls=[0]
for i in stdin:
	i=i.strip().split();
	if(i[0]=="/assets/js/the-associates.js"):
		ls[0]+=1
print(ls[0]);
