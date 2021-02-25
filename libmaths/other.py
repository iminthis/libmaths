#Author : Vinay Venkatesh
#Date : 2/20/2021

import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(x):

    return 1 / (1 + np.exp(-x))

def relu(x):

  return np.maximum(0, x)

def isPrime(*integers):
  for value in integers:
    if value > 1:
    
      
      for i in range(2, int((value / 2))+1):
    

        if (value % i) == 0:
          output = False
          print(value, output)
          break
      else:
        output = True
        print(value, output)

def isSquare(*integers):

  for value in integers: 
    if value >= 0:
      sr = math.sqrt(value)
          
      #return boolean T/F
      if sr**2 == value:
        output = True
        print(value, output)
        return output
      else:
        output = False
        print(value, output)
        return output

def divisor(x):

  count = 0

  for i in range(1, x+1):
    
    if x % i == 0:
      
      count += 1

  return(count)
