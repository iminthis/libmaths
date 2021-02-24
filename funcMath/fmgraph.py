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

def quadratic(a, b, c):

  '''
  In algebra, a quadratic function, a quadratic polynomial, a 
  polynomial of degree 2, or simply a quadratic, is a polynomial 
  function with one or more variables in which the highest-degree term is of the second degree. 

  The difference between `quadratic()` and `vtquadratic()` is the forms of the quadratic functions.
  `quadratic()` is meant to be in a ax^2 + bx + c form and `vtquadratic()` is meant to be in a a(x - h)^2 + k form.

  Learn More: https://www.mathsisfun.com/algebra/quadratic-equation.html
  '''

  #Y = AX^2 + BX + C
  if a == 0:
    print("a cannot be 0")
  x = np.linspace(-6,6,100)

  # the function, which is y = x^2 here
  y = a*x**2 + b*x + c
  vertex = (-1 * b) / (2 * a)
  vertex = a * vertex ** 2 + b * vertex + c

  # setting the axes at the centre
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  if c < 0 and a < 0:
    plt.ylim((vertex + (2 * vertex), vertex * -1 + 1))
  if c < 0:
    plt.ylim((vertex -1, vertex * -1 + 1))
  elif c > 0 and c <= 999:
    plt.ylim((-5,c+c+5))
  elif c == 0:
    plt.ylim((-5,5))
  elif c >= 1000 and c <= 5000:
    plt.ylim((0,c*10))
    x = np.linspace(-20,20,100)
  elif c >= 5001 and c <= 20000:
    plt.ylim((0,c*10))
    x = np.linspace(-20,20,100)
  elif c >= 20001:
    plt.ylim((0,c*2))
    x = np.linspace(-20,20,100)
  # plot the function

  else:
    numList = []
    numList.append(a)
    numList.append(b)
    numList.append(c)
    for i in range(0, len(numList)):
      if numList[i] < 0:
        numList[i] = -1 * numList[i]

    plt.ylim((-1 * max(numList) * 5, max(numList) * 5))
  
  plt.plot(x,y, 'r', label=f'{a}x^2+{b}x+{c}')
  plt.title(f'Quadratic Graph')
  # show the plot
  
  plt.show()

  print(f"Vertex: ({(-1 * b)/(2 * a)}, {vertex})")
  print(f"Y-Intercept: (0, {c})")

  x, y = symbols('x y')

  equation = Eq(y, a*x**2 + b*x + c)

  # Use sympy.subs() method
  result = solve(equation.subs(y, 0))

  for i in range(0, len(result)):
    result[i] = round(result[i].simplify().evalf(),3)

  #print(result)
  if len(result) == 2:
    print(f"X-Intercept: ({result[0]}, 0), ({result[1]}, 0)")
  elif len(result) == 1:
    print(f"X-Intercept: ({result[0]}, 0)")

def vtquadratic(a, h, k):

  '''
  In algebra, a quadratic function, a quadratic polynomial, a 
  polynomial of degree 2, or simply a quadratic, is a polynomial 
  function with one or more variables in which the highest-degree term is of the second degree. 

  The difference between `quadratic()` and `vtquadratic()` is the forms of the quadratic functions.
  `quadratic()` is meant to be in a ax^2 + bx + c form and `vtquadratic()` is meant to be in a a(x - h)^2 + k form.

  Learn More: https://www.mathsisfun.com/algebra/quadratic-equation.html
  '''

  #y = a(x - h)^2 + k
  if a == 0:
    print("a cannot be 0")

  if h < 0:
    x = np.linspace(h-5, (-1 * h) + 5,100)
  elif k < 0:
    x = np.linspace(k*2, -k*3,100)
  else:
    x = np.linspace(-6,6,100)
  y = a * (x - h)**2 + k
  vertexX = h
  vertexY = k
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')

  if k < 0 and h < 0:
    plt.ylim((k + (2 * k), k * -1 + 1))
  elif a < 0 and k < 0:
    plt.ylim((k*3, 0))
  elif k < 0:
    plt.ylim((k * 1.5, -k * 1.5))
  elif k > 0 and k <= 999:
    plt.ylim((-k*3,k*3))
    #x = np.linspace(-20,20,100)
  elif k == 0:
    plt.ylim((-5,5))
  elif k >= 1000 and k <= 5000:
    plt.ylim((0,k*5))
    x = np.linspace(-100,100,100)
  elif k >= 5001 and k <= 20000:
    plt.ylim((0,k*3))
    x = np.linspace(-100,100,100)
  elif k >= 20001:
    plt.ylim((0,k*3))
    x = np.linspace(-100,100,100)

  else:
    numList = []
    numList.append(a)
    numList.append(h)
    numList.append(k)
    for i in range(0, len(numList)):
      if numList[i] < 0:
        numList[i] = -1 * numList[i]

    plt.ylim((-1 * max(numList) * 5, max(numList) * 5))

  # plot the function
  plt.plot(x,y, 'r', label=f'{a}(x-{h})^2+{k}')
  plt.title(f'Quadratic Graph')

  plt.show()

  print(f"Vertex: ({round(h,3)}, {round(k,3)})")
  print(f"Y-Intercept: (0, {round(a*(0-h)**2+k,3)})")

  x, y = symbols('x y')

  equation = Eq(y, a * (x - h)**2 + k)

  # Use sympy.subs() method
  result = solve(equation.subs(y, 0))
  #print(result)
  for i in range(0, len(result)):
    result[i] = result[i].simplify().evalf()
    try:
      result[i] = round(result[i], 3)
    except:
      pass

  if len(result) == 2:
    print(f"X-Intercept: ({result[0]}, 0), ({result[1]}, 0)")
  elif len(result) == 1:
    print(f"X-Intercept: ({result[0]}, 0)")

def cubic(a, b, c, d):

  '''
  In mathematics, a cubic function is a function of the form f(x)=ax^3+bx^2+cx+d 
  where the coefficients a, b, c, and d are real numbers, and the variable x takes real values, 
  and a ≠ 0. In other words, it is both a polynomial function of degree three, and a real function.

  Learn More: https://www.varsitytutors.com/hotmath/hotmath_help/topics/cubic-functions
  '''

  #ax^3+bx^2+cx+d
  if a == 0:
    print("a cannot be 0")

  x = np.linspace(-6,6,100)
  if d >= 1000:
    x = np.linspace(-100,100,100)

  # the function, which is y = x^2 here
  y = a * x**3 + b * x**2 + c * x + d

  # setting the axes at the centre
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')

  if d == 0:
    plt.ylim((-5,5))
  elif b < 0 and c < 0 and d < 0:
    if -b > -c and -b > -d:
      plt.ylim((b*5,-b*5))
    elif -c > -b and -c > -d:
      plt.ylim((c*5,-c*5))
    elif -d > -c and -d > -b:
      plt.ylim((d*5,-d*5))
  elif d > 0 and c < 0:
    plt.ylim((-d*5,d*5))
  elif c > 0 and d < 0:
    if c > -d:
      plt.ylim((c*4,-c*4))
    else:
      plt.ylim((d*4,-d*4))
  elif d < 0:
    plt.ylim((d*4,-d*4))
  elif d > 0 and c > 0:
    if d > c or d == c:
      plt.ylim((-d*5,d*5))
  elif d > 0 and d <= 999:
    plt.ylim((-d*3.5,d*3.5))
  elif d >= 1000 and d <= 5000:
    plt.ylim((-d*5,d*5))
    #x = np.linspace(-100,100,100)
  elif d >= 5001 and d <= 20000:
    plt.ylim((0,d*3))
    #x = np.linspace(-100,100,100)
  elif d >= 20001:
    plt.ylim((0,d*3))
    #x = np.linspace(-100,100,100)

  else:
    numList = []
    numList.append(a)
    numList.append(b)
    numList.append(c)
    numList.append(d)
    for i in range(0, len(numList)):
      if numList[i] < 0:
        numList[i] = -1 * numList[i]

    plt.ylim((-1 * max(numList) * 5, max(numList) * 5))  

  # plot the function
  plt.plot(x,y, 'r', label=f'{a}x^3+{b}x^2+{c}x+{d}')
  plt.title(f'Cubic Graph')

  plt.show()

  '''vertX = (-b) / (2 * a)
  vertY = a * vertX**3 + b * vertX**2 + c*vertX + d
  print(f"Vertex: ({vertX}, {vertY})")'''
  print(f"Y-Intercept: (0, {d})")

  x, y = symbols('x y')

  equation = Eq(y, a * x**3 + b * x**2 + c * x + d)

  # Use sympy.subs() method
  result = solve(equation.subs(y, 0))
  for i in range(0, len(result)):
    result[i] = result[i].simplify().evalf()
    try:
      result[i] = round(result[i], 3)
    except:
      pass

  if len(result) == 1:
    print(f"X-Intercept(s): ({result[0]}, 0)")
  if len(result) == 2:
    print(f"X-Intercept(s): ({result[0]}, 0), ({result[1]}, 0)")
  if len(result) == 3:
    print(f"X-Intercept(s): ({result[0]}, 0), ({result[1]}, 0), ({result[2]}, 0)")

def trigsin(z, b):

  '''
  In mathematics, the trigonometric functions are real functions which relate
  an angle of a right-angled triangle to ratios of two side lengths. 

  Learn More: https://www.mathsisfun.com/sine-cosine-tangent.html
  '''

  x = np.linspace(-np.pi,np.pi,100)

  # the function, which is y = sin(x) here
  y = z * np.sin(b * x)
  yint = z * np.sin(b * 0)

  # setting the axes at the centre
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('center')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  if z < 0:
    plt.ylim((z*1.5,-z*1.5))
  else:
    plt.ylim((-z*1.5,z*1.5))
  # plot the functions
  plt.plot(x,y, 'b', label=f'y={z}sin({b}x)')
  plt.title('Sine Graph')
  plt.legend(loc='upper left')

  # show the plot
  plt.show()

def trigcos(z, b):

  '''
  In mathematics, the trigonometric functions are real functions which relate
  an angle of a right-angled triangle to ratios of two side lengths. 

  Learn More: https://www.mathsisfun.com/sine-cosine-tangent.html
  '''
  
  x = np.linspace(-np.pi,np.pi,100)

  # the function, which is y = sin(x) here
  y = z * np.cos(b * x)

  # setting the axes at the centre
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('center')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  if z < 0:
    plt.ylim((z*1.5,-z*1.5))
  else:
    plt.ylim((-z*1.5,z*1.5))
  # plot the functions
  plt.plot(x,y, 'b', label=f'y={z}cos({b}x)')
  plt.title('Cosine Graph')
  plt.legend(loc='upper left')

  # show the plot
  plt.show()

def trigtan(z, b):

  '''
  In mathematics, the trigonometric functions are real functions which relate
  an angle of a right-angled triangle to ratios of two side lengths. 

  Learn More: https://www.mathsisfun.com/sine-cosine-tangent.html
  '''

  x = np.linspace(-np.pi,np.pi,100)

  # the function, which is y = sin(x) here
  y = z * np.tan(b * x)

  # setting the axes at the centre
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('center')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  if z < 0:
    plt.ylim((z*1.5,-z*1.5))
  else:
    plt.ylim((-z*1.5,z*1.5))
  # plot the functions
  plt.plot(x,y, 'b', label=f'y={z}tan({b}x)')
  plt.title('Tangent Graph')
  plt.legend(loc='upper left')

  # show the plot
  plt.show()

def quartic(a, b, c, d, e):

  '''
  In algebra, a quartic function is a function of the form f(x)=ax^{4}+bx^{3}+cx^{2}+dx+e, 
  where a is nonzero, which is defined by a polynomial of degree four, called a quartic polynomial.

  Learn More: https://www.calculushowto.com/types-of-functions/quartic-function/
  '''

  if a == 0:
    print("a cannot be 0")

  x = np.linspace(-6,6,100)
  if b <= -18 and b >= -29:
    x = np.linspace(b,-b,100)
  elif b <= -30:
    x = np.linspace(b/2, -b/2, 100)
  elif b >= 10 and b <= 29:
    x = np.linspace(b,-b,100)
  elif b >= 30:
    x = np.linspace(b/2, -b/2, 100)

  # the function, which is y = x^2 here
  y = a * x**4 + b * x**3 + c * x**2 + d*x + e

  # setting the axes at the centre
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  
  #positive constraints
  if b >= -5 and b <= 0:
    plt.ylim((-6,6))
  elif b < -5 and b >= -9:
    plt.ylim((b*3,-b*3))
  elif b < -9 and b > -16:
    plt.ylim((b*-b,-b*-b))
  elif b <= -16 and b >= -27:
    plt.ylim((b*-b*3,-b*-b*3))
  elif b <= -28 and b >= -35:
    plt.ylim((b*-b*5,-b*-b*5))
  elif b <= -35 and b >= -120:
    plt.ylim((b*-b*-b/2,-b*-b*-b/2))
  elif b <= -121:
    plt.ylim((b*-b*-b,-b*-b*-b))


  #negative constraints
  elif b <= 5 and b >= 0:
    plt.ylim((-6,6))
  elif b > 5 and b <= 9:
    plt.ylim((-b*3,b*3))
  elif b > 9 and b < 16:
    plt.ylim((b*-b,-b*-b))
  elif b >= 16 and b <= 27:
    plt.ylim((b*-b*3,-b*-b*3))
  elif b >= 28 and b <= 35:
    plt.ylim((b*-b*5,-b*-b*5))
  elif b >= 35 and b <= 120:
    plt.ylim((b*b*-b/2,-b*b*-b/2))
  elif b >= 121:
    plt.ylim((b*-b*-b,-b*-b*-b))

  if e == 0:
    plt.ylim((-5,5))
  elif e > b:
    plt.ylim((-e*2,e*2))
  elif e * -1 > b * -1:
    plt.ylim((e*2,-e*2))
  
  else:
    numList = []
    numList.append(a)
    numList.append(b)
    numList.append(c)
    numList.append(d)
    numList.append(e)
    for i in range(0, len(numList)):
      if numList[i] < 0:
        numList[i] = -1 * numList[i]

    plt.ylim((-1 * max(numList) * 5, max(numList) * 5))

  #plt.ylim((-5,5))
  # plot the function
  plt.plot(x,y, 'r', label=f'{a}x^4+{b}x^3+{c}x^2+{d}x+{e}')
  plt.title('Quartic Graph')

  plt.show()

  print(f"Y-Intercept: (0, {e})")

  x, y = symbols('x y')

  equation = Eq(y, a * x**4 + b * x**3 + c * x**2 + d*x + e)

  # Use sympy.subs() method
  result = solve(equation.subs(y, 0))
  for i in range(0, len(result)):
    result[i] = result[i].simplify().evalf()
    try:
      result[i] = round(result[i], 3)
    except:
      pass

  print(f"X-Intercept(s): ")
  for i in range(0, len(result)):
    print(f"({result[i]}, 0)")

def quintic(a, b, c, d, e, f):

  '''
  In algebra, a quintic function is a function of the form g(x)=ax^{5}+bx^{4}+cx^{3}+dx^{2}+ex+f,
  where a, b, c, d, e and f are members of a field, typically the rational numbers, the real numbers or the complex numbers, 
  and a is nonzero. In other words, a quintic function is defined by a polynomial of degree five.

  Learn More: https://www.calculushowto.com/quintic-function-polynomial/
  '''

  if a == 0:
    print("a cannot be 0")

  x = np.linspace(-6,6,100)
  if b <= -18 and b >= -29:
    x = np.linspace(b,-b,100)
  elif b <= -30:
    x = np.linspace(b/2, -b/2, 100)
  elif b >= 10 and b <= 29:
    x = np.linspace(b,-b,100)
  elif b >= 30:
    x = np.linspace(b/2, -b/2, 100)

  # the function, which is y = x^2 here
  y = a * x**5 + b * x**4 + c * x**3 + d*x**2 + e*x + f

  # setting the axes at the centre
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')

  if b >= 10 and b <= 29:
    plt.ylim((-b*5,b*5))

  else:
    numList = []
    numList.append(a)
    numList.append(b)
    numList.append(c)
    numList.append(d)
    numList.append(e)
    numList.append(f)
    for i in range(0, len(numList)):
      if numList[i] < 0:
        numList[i] = -1 * numList[i]

    plt.ylim((-1 * max(numList) * 5, max(numList) * 5))

  plt.plot(x,y, 'r', label=f'{a}x^5+{b}x^4+{c}x^3+{d}x^2+{e}x+{f}')
  plt.title('Quintic Graph')

  plt.show()

  print(f"Y-Intercept: (0, {f})")

  x, y = symbols('x y')

  equation = Eq(y, a * x**5 + b * x**4 + c * x**3 + d*x**2 + e*x + f)

  # Use sympy.subs() method
  result = solve(equation.subs(y, 0))
  for i in range(0, len(result)):
    result[i] = result[i].simplify().evalf()
    try:
      result[i] = round(result[i], 3)
    except:
      pass

  print(f"X-Intercept(s): ")
  for i in range(0, len(result)):
    print(f"({result[i]}, 0)")

def sextic(a, b, c, d, e, f, g):

  '''
  A sextic function is a function defined by a sextic polynomial. Because they have an even degree,
  sextic functions appear similar to quartic functions when graphed, except they may possess an additional local
  maximum and local minimum each. The derivative of a sextic function is a quintic function.

  Learn More: https://www.calculushowto.com/sextic-function/
  '''

  if a == 0:
    print("a cannot be 0")

  x = np.linspace(-6,6,100)
  if b <= -18 and b >= -29:
    x = np.linspace(b,-b,100)
  elif b <= -30:
    x = np.linspace(b/2, -b/2, 100)
  elif b >= 10 and b <= 29:
    x = np.linspace(b,-b,100)
  elif b >= 30:
    x = np.linspace(b/2, -b/2, 100)

  # the function, which is y = x^2 here
  y = a * x**6 + b * x**5 + c * x**4 + d*x**3 + e*x**2 + f*x + g

  # setting the axes at the centre
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')

  numList = []
  numList.append(a)
  numList.append(b)
  numList.append(c)
  numList.append(d)
  numList.append(e)
  numList.append(f)
  numList.append(g)
  for i in range(0, len(numList)):
    if numList[i] < 0:
      numList[i] = -1 * numList[i]

  plt.ylim((-1 * max(numList) * 5, max(numList) * 5))

  plt.plot(x,y, 'r', label=f'{a}x^6+{b}x^5+{c}x^4+{d}x^3+{e}x^2+{f}x+{g}')
  plt.title('Sextic Graph')

  plt.show()

  print(f"Y-Intercept: (0, {g})")

  x, y = symbols('x y')

  equation = Eq(y, a * x**6 + b * x**5 + c * x**4 + d*x**3 + e*x**2 + f*x + g)

  # Use sympy.subs() method
  result = solve(equation.subs(y, 0))
  for i in range(0, len(result)):
    result[i] = result[i].simplify().evalf()
    try:
      result[i] = round(result[i], 3)
    except:
      pass

  print(f"X-Intercept(s): ")
  for i in range(0, len(result)):
    print(f"({result[i]}, 0)")

def logFun(a, b):

  '''
  Logarithm (log) In mathematics, the logarithm is the inverse function to exponentiation.
  That means the logarithm of a given number x is the exponent to which another fixed number,
  the base b, must be raised, to produce that number x.

  Learn More: https://www.mathsisfun.com/sets/function-logarithmic.html
  '''

  if a == 0:
    print("a cannot be 0")
  elif b == 0:
    print("b cannot be 0")

  x = np.linspace(-6,6,100)

  # the function, which is y = x^2 here
  y = a * np.log(b * x)

  fig = plt.figure()

  numList = []
  numList.append(a)
  numList.append(b)
  for i in range(0, len(numList)):
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
    print("a cannot be 0")
  elif b == 0:
    print("b cannot be 0")

  numList = []
  numList.append(a)
  numList.append(b)
  numList.append(c)
  for i in range(0, len(numList)):
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
