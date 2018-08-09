#!/usr/bin/python
from sys import *;
from operator import *;
oldvalue=None;
oldpath=None
ls=[0]
dic=dict()
dicpath=dict();
for i in stdin:
	i=i.strip().split("\t");
	if(len(i)!=2):
		continue;
	currentpath,name=i;
	#print("{0}\t{1}".format(i[0],i[1]))
	if(oldvalue and oldvalue!=name):
		dic[oldvalue]=ls[0]
		dicpath[oldvalue]=oldpath;
		ls[0]=0;
	oldvalue=name
	oldpath=currentpath
	ls[0]+=1;
if oldvalue:
	dic[oldvalue]=ls[0];
	dicpath[oldvalue]=oldpath;
	

result=sorted(dic.items(),key=itemgetter(1),reverse=True);
rskeys=result[0][0];
rspath=dicpath[rskeys];
finalfreq=dic[rskeys];
print("{0}\t{1}\t{2}".format(rskeys,rspath,finalfreq));
