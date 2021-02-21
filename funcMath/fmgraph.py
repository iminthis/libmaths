import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def sigmoid():
  x = np.linspace(-10, 10, 100) 
  z = 1/(1 + np.exp(-x)) 
    
  plt.plot(x, z) 
  plt.xlabel("x") 
  plt.ylabel("Sigmoid(X)") 
    
  plt.show() 

def relu():
  x = np.linspace(-10, 10, 100) 
  z = np.maximum(0, x) 
    
  plt.plot(x, z) 
  plt.xlabel("x") 
  plt.ylabel("Sigmoid(X)") 
    
  plt.show() 

def constant(c):

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

# 100 linearly spaced numbers
def quadratic(a, b, c):
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

