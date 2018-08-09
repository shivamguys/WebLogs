#!/usr/bin/python
from sys import *;
count=0;
for i in stdin:
	
	i=i.strip().split(" ");
# i will be passing only this ip adress to reduce the overhead
	if(i[0]=="10.99.99.186"):	
		count+=1;
print(count)
