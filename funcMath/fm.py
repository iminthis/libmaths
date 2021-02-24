#Author : Vinay Venkatesh
#Date : 2/20/2021

import numpy as np
import math

def sigmoid(x):
  
    return 1 / (1 + np.exp(-x))

def relu(x):

  return np.maximum(0, x)

def isPrime(*integers):
  for value in integers:
    if value > 1:
    
        # Iterate from 2 to n / 2
        for i in range(2, value):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (value % i) == 0:
                print(value, "is not a prime number")
                break
        else:
            print(value, "is a prime number")
    
    else:
        print(value, "is not a prime number")

def isSquare(*integers):
 
    #if x >= 0,
    for value in integers: 
      if value >= 0:
          sr = math.sqrt(value)
          
          #return boolean T/F
          if sr**2 == value:
            print(value, "is a perfect square")
          else:
            print(value, "is not a perfect square")