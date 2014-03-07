#!/usr/bin/python
#!encoding: UTF-8
n = int (raw_input('Numero de subintervalos: '))
sumatorio = 0.0
for i in range (0, n):
  print 'Subintervalos:'
  print (i*(1/float(n)), (i+1)*(1/float(n)))
  xi = (i*(1/float(n))+(i+1)*(1/float(n)))/2
  print 'x_i:' 
  print xi
  print 'fx_i:' 
  print 4/(1 + (xi**2)) 
  sumatorio += 4/(1 + (xi**2))
a = (1/float(n))*sumatorio
print 'El valor aproximado de PI es: %.15f' % a
from math import pi
print 'El valor de PI con 35 decimales: %.35f' % pi
