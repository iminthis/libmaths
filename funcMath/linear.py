#Developer : Vinay Venkatesh
#Date : 2/20/2021

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

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

def constant(c):

    '''
    A constant function is a function whose value is the same for every input value.
    With a constant function, for any two points in the interval, a change in x results in a zero change in f(x).

    Learn More: https://www.varsitytutors.com/hotmath/hotmath_help/topics/constant-function
    '''

    fig = plt.figure()
    # Hold activation for multiple lines on same graph
    # Set x-axis range
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.xlim((-1 * (c + c), c + c))
    # Set y-axis range
    plt.ylim((-1 * (c + c), c + c))
    # Draw lines to split quadrants

    plt.axhline(y = c)

    plt.title('Constant Graph')

    plt.show()

def linear(m, b):

  '''
  A linear function is a function whose graph is a straight line.
  A linear function has one independent variable and one dependent variable. 
  The independent variable is x and the dependent variable is y. 
  The inputs, m and b stand for the slope and y intercept.

  The difference between `linear()` and `psflinear()` is the forms of the linear functions.
  `psflinear()` is meant to be in a y - y1 = m(x - x1) form and `linear()` is meant to be in a y = mx+b form.

  Learn More: https://www.mathsisfun.com/algebra/linear-equations.html
  '''

  #y = mx + b
  x = np.linspace(-5,5,100)
  y = m*x+b
  plt.plot(x, y, '-r', label=f'y={m}x+{b}')
  plt.title(f'Linear Graph')
  plt.xlabel('x', color='#1C2833')
  plt.ylabel('y', color='#1C2833')
  plt.legend(loc='upper left')
  plt.grid()
  plt.show()

  x, y = symbols('x y')

  equation = Eq(y, m*x+b)

  # Use sympy.subs() method
  result = solve(equation.subs(y, 0))

  for i in range(0, len(result)):
    result[i] = round(result[i].simplify().evalf(),3)

  print(f"Slope: {m}")
  print(f"Y-Intercept: (0, {b})")
  print(f"X-Intercept: ")
  for i in range(0, len(result)):
    print(f"({result[i]}, 0)")

def psflinear(y1, m, x1):

  '''
  A linear function is a function whose graph is a straight line.
  A linear function has one independent variable and one dependent variable. 
  The independent variable is x and the dependent variable is y. 
  The inputs, y1 and m and x1 stand for a y coordinate, slope, and x coordinate.

  The difference between `psflinear()` and `linear()` is the forms of the linear functions.
  `psflinear()` is meant to be in a y - y1 = m(x - x1) form and `linear()` is meant to be in a y = mx+b form.

  Learn More: https://www.mathsisfun.com/algebra/linear-equations.html
  '''

  #y - y1 = m(x - x1)
  x = np.linspace(-5,5,100)
  y = m * (x - x1) + y1
  plt.plot(x, y, '-r', label=f'y-{y1}={m}(x-{x1})')
  plt.title(f'Linear Graph')
  plt.xlabel('x', color='#1C2833')
  plt.ylabel('y', color='#1C2833')
  plt.legend(loc='upper left')
  plt.grid()
  plt.show()

  x, y = symbols('x y')

  equation = Eq(y, m*(x-x1)+y1)

  # Use sympy.subs() method
  result = solve(equation.subs(y, 0))

  for i in range(0, len(result)):
    result[i] = round(result[i].simplify().evalf(),3)

  print(f"Slope: {m}")
  print(f"Y-Intercept: (0, {y1})")
  print(f"X-Intercept: ")
  for i in range(0, len(result)):
    print(f"({result[i]}, 0)")

