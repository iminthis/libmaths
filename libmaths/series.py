import numpy as np
import matplotlib.plt as plt

def arithmetic(i, params):
    '''
    params is a two element array

    params[0]: the initial term 
    params[1]: the common difference
    '''
    return params[0]+(i-1)*params[1]

def geometric(i, params):
    '''
    params is a two element array

    params[0]: the initial term
    params[1]: the common ratio
    '''
    return params[0]*params[1]**(i-1)

def harmonic(i, params):
    '''
    params is a two element array

    params[0]: the initial term
    params[1]: the common difference
    '''
    return 1/(params[0]+(i-1)*params[1])

class Series:
    '''
    Template for any mathematical series.
    Author: Atharva Naik
    Website (https://atharva-naik.github.io/)
    '''
    def __init__(self, general_term=None, general_term_str=None, params=[]): 
        self.term_function = general_term # usually a python function. 
        self.sum_function = None
        self.product_function = None
        self.params = params
        self.term_str = ""
        self.sum_str = ""
        self.product_str = ""

    def eval(self, i):
        '''
        Evaluate the general term of the series
        at index i
        '''
        return self.term_function(i, self.params)

    def sum(self, i_0=1, n=10):
        '''
        i_0: is the first term from which summation begins
        n: is the term till which summation is carried out
        ∑ⁿ f(x) where f(x) is the general term
        '''
        if self.sum_function:
            return self.sum_function(n, self.params)
        else:
            sum_n = 0
            for i in range(i_0, n+1):
                sum_n += self.term_function(i, self.params)
            
            return sum_n

    def product(self, i_0=1, n=10):
        '''
        i_0: is the first term from which product begins
        n: is the term till which product is carried out
        ∏ⁿ f(x) where f(x) is the general term
        '''
        if self.product_function:
            return self.product_function(n, self.params)
        else:
            prod_n = 0
            for i in range(i_0, n+1):
                prod_n *= self.term_function(i, self.params)
            
            return prod_n

    def plot(self, i_0, n=10):
        '''
        Plot terms of the series from then index i₀ to n
        '''
        x,y = [], []
        for i in range(i_0, n+1):
            x.append(i)
            y.append(self.eval(i))

    def plot_sum(self, i_0, n=10):
        '''
        Plot sum of the series from then index i₀ to n
        '''
        x,y = [], []
        for i in range(i_0, n+1):
            x.append(i)
            y.append(self.sum(i))

class ArithmeticSeries(Series):
    pass 

class GeometricSeries(Series):
    pass 

class HarmonicSeries(Series):
    pass 
