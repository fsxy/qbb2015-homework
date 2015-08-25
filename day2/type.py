#!/usr/bin/env python

#Integer
i=10000


#String
s="A String"


#float

f=0.04

f_i=int(f)
i_f=float(i)

#Boolean
truthy=True
falsy=False

#Dictionary

dic1={
    "key1":"value1",
    "key2":"value2"
}
dic2=dict(key1="value1",key2="value2")       
dic3=dict([("key1","value1"),("key2","value2")])       #dic1 is the same as dic2 and dic3.

#List  --conventionally contains only one type
l=[1,2,3,4,5]
l.append(7)

#Tuple  elements can have different types
t=(1,"foo",5.0)   #Tuples can't be changed


for value in (i,s,f,f_i,i_f,truthy,falsy,dic1,dic2,dic3,l,t):
    print value, type(value)