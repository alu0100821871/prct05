#!/usr/bin/python
#!encoding: UTF-8
n = int (raw_input('Numero de subintervalos: '))
sumatorio = 0.0
for i in range (1, n+1):
  a = (i-1)/float(n)
  b = i/float(n)
  xi = (i-0.5)/float(n)
  fxi = 4/(1 + (xi**2))
  print 'Subintervalos: [%.2f %.2f] x_i: %.3f fx_i: %f' % (a, b, xi, fxi) 
  sumatorio += fxi
c = sumatorio/float(n)
print 'El valor aproximado de PI es: %.35f' % c
from math import pi
print 'El valor de PI con 35 decimales: %.35f' % pi