#!/usr/bin/python
from sys import *;
a=None
for i in stdin:
	i=i.strip().split(" ");
	#print("{0}".format(len(i)));
	#i=i.split("");
	s=i[6].strip('" ').split("/"); #this is the working phase
	if(s[len(s)-1]!="" and '.' in s[len(s)-1]):	
		#print(s[len(s)-1]);
		new=""
		
		for j in s[0:len(s)-1]:
			if("http" in j or "www" in j):
				continue;
			else:
				new+=j+" ";
		
		new=new.replace(" ",'/');
		#if(new!="/"):		
		print("{0}\t{1}".format(new,s[len(s)-1]))
	#if(s[len(s)-1]==""):
	#	print(s);
