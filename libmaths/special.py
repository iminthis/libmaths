#Developer : Vinay Venkatesh
#Date : 2/20/2021

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def logFun(a, b):

  '''
  Logarithm (log) In mathematics, the logarithm is the inverse function to exponentiation.
  That means the logarithm of a given number x is the exponent to which another fixed number,
  the base b, must be raised, to produce that number x.

  Learn More: https://www.mathsisfun.com/sets/function-logarithmic.html
  '''

  if a == 0:
    raise ValueError("a cannot be 0")
  elif b == 0:
    raise ValueError("b cannot be 0")

  x = np.linspace(-6,6,100)

  # the function, which is y = x^2 here
  y = a * np.log(b * x)

  fig = plt.figure()

  numList = [a, b]
  for i in range(len(numList)):
    if numList[i] < 0:
      numList[i] = -1 * numList[i]

  plt.ylim((-1 * max(numList) * 5, max(numList) * 5))

  plt.plot(x,y, 'r') #label=f'{a}x^6+{b}x^5+{c}x^4+{d}x^3+{e}x^2+{f}x+{g}')
  plt.title('Log Graph')

  plt.show()

def absVal(a, b, c):

  '''
  An absolute value function is a function that contains an algebraic expression within absolute value symbols. 

  Learn More: https://www.varsitytutors.com/hotmath/hotmath_help/topics/absolute-value-functions
  '''

  if a == 0:
    raise ValueError("a cannot be 0")
  elif b == 0:
    raise ValueError("b cannot be 0")

  numList = [a, b, c]
  for i in range(len(numList)):
    if numList[i] < 0:
      numList[i] = -1 * numList[i]

  fig = plt.figure()

  plt.ylim((-1 * max(numList) * 5, max(numList) * 5))
  x = np.linspace(-5 * max(numList),max(numList)*5,100)
  # the function, which is y = x^2 here
  y = a * abs(b + x) + c

  plt.plot(x,y, 'r') #label=f'{a}x^6+{b}x^5+{c}x^4+{d}x^3+{e}x^2+{f}x+{g}')
  plt.title('Absolute Value Graph')

  plt.show()

def sigmoid():

  '''
  In the context of artificial neural networks, the Sigmoid Function is a type of activation function. The Sigmoid Function is often referred
  to as a squashing function because it limits its outputs to a range between 0 and 1. The Sigmoid Function has an "S" - shaped curve or sigmoid curve.

  This function was intended to be only for visualizing the graph of a sigmoid function.

  Learn More: https://deepai.org/machine-learning-glossary-and-terms/sigmoid-function
  '''

  x = np.linspace(-10, 10, 100) 
  z = 1/(1 + np.exp(-x)) 
    
  plt.plot(x, z) 
  plt.xlabel("x") 
  plt.ylabel("Sigmoid(X)") 
    
  plt.show() 

def relu():

  '''
  In the context of artificial neural networks, the ReLu Function is a type of activation function. The ReLu function directly outputs its input
  if it is positive. Otherwise, it outputs 0.

  This function was intended to be only for visualizing the graph of a ReLu function.

  Learn More: https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/#.
  '''

  x = np.linspace(-10, 10, 100) 
  z = np.maximum(0, x) 
    
  plt.plot(x, z) 
  plt.xlabel("x") 
  plt.ylabel("ReLu(X)") 
    
  plt.show()