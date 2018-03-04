#! /usr/bin/python
import random,re

def f1(x,y=0):
    return x**2 + y

def f2(a):
    if a == []:
     return "BUUUM"
    else:
     return a[0]
def f3(b):
    if b == 1:
        return "jeden"
    elif b == 2:
        return "dwa"
    elif b == 3:
       return "trzy"
    elif b:
        return "other"

def f4(c,d=0):
    if  d == 0:
        return "%s ma kota"%c
    else:
        return "%s ma kota i %s" %(c,d)

def f5(e, f=1):
    lista=[]
    for i in range(17)[0:e:f]:
        lista.append(i)
    return lista

    #return range(e)[0:e:f]

def f6(g,h):
        return g*h

def f7(i):

    if re.match('[a-z]+',i):
        return "slowo"
    elif re.match('[0-9][0-9]+',i):
            return "liczba"
    elif re.match('[0-9]',i):
        return "cyfra"
    elif re.match('[-0-9][0-9]+',i):
        return "liczba ze znakiem"
    elif re.match('[A-Z, a-z, ,.]+',i):
        return "zdanie"
