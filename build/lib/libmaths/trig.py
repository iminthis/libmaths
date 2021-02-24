#Developer : Vinay Venkatesh
#Date : 2/20/2021

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

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