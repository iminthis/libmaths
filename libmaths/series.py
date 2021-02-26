# Atharva Naik
# Feb 26, 2021

import numpy as np
import matplotlib.pyplot as plt

def identity(x):
    '''
    Simply returns x
    Default value for general term in series
    '''
    return x

def arithmetic(i, params):
    '''
    params is a two element array

    params[0]: the initial term 
    params[1]: the common difference
    '''
    return params[0]+(i-1)*params[1]

def arithmetic_sum(n, params):
    '''
    params is a two element array

    params[0]: the initial term 
    params[1]: the common difference
    '''
    if n == 0:
        return 0
    return (n)*(2*params[0]+(n-1)*params[1])/2

def geometric(i, params):
    '''
    params is a two element array

    params[0]: the initial term
    params[1]: the common ratio
    '''
    return params[0]*params[1]**(i-1)

def geometric_sum(n, params):
    '''
    params is a two element array

    params[0]: the initial term 
    params[1]: the common difference
    '''
    if n == 0:
        return 0
    return (params[0])*(params[1]**n-1)/(params[1]-1)

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
    def __init__(self, general_term=identity, general_term_str=None, params=[]): 
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

    def sum(self, n=10, i_0=1):
        '''
        i_0: is the first term from which summation begins
        n: is the term till which summation is carried out
        ∑ⁿ f(x) where f(x) is the general term
        '''
        if self.sum_function:
            return self.sum_function(n, self.params)-self.sum_function(i_0-1, self.params)
        else:
            sum_n = 0
            for i in range(i_0, n+1):
                sum_n += self.term_function(i, self.params)
            
            return sum_n

    def product(self, n=10, i_0=1):
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

    @classmethod
    def gen(cls, params, general_term=None, start=1, end=10):
        ''' 
        This is a class method. This means an object doesn't need to 
        be created for this. It functions like a generator. This helps in iterating
        over terms of the series (like range, but for any term_function)

        e.g. usage: Series.gen(params=[1, 2], general_term=arithmetic, start=1, end=5)
        '''
        cls.params = params
        cls.term_function = general_term
        for i in range(start, end+1):
            yield cls.term_function(i, cls.params)

    def plot_sum(self, i_0, n=10):
        '''
        Plot sum of the series from then index i₀ to n
        '''
        x,y = [], []
        for i in range(i_0, n+1):
            x.append(i)
            y.append(self.sum(i))

class ArithmeticSeries(Series):
    '''
    Creates arithmetic series with first term first_term 
    and common difference common_difference
    '''
    def __init__(self, first_term=1, common_difference=1):
        '''
        we set the term_function to arithmetic 
        the sum function to n*(2a+(n-1)*d)/2 (this makes taking the sum 𝓞(1) instead of 𝓞(n))
        '''
        self.term_function = arithmetic
        self.params = []
        self.params.append(first_term)
        self.params.append(common_difference)
        self.sum_function = arithmetic_sum
        self.term_str = "tᵢ=a-d+d×i, i∈ {1,2 …}".replace("a-d", str(round(first_term-common_difference, 2))).replace("d", str(round(common_difference, 2)))
        self.sum_str = "Sᵢ=ⁿ⁄₂(2a-d+d×n), n∈ {1,2 …}".replace("2a-d", str(round(2*first_term-common_difference, 2))).replace("d", str(round(common_difference, 2)))

    @classmethod
    def gen(cls, n, first_term=1, common_difference=1):
        '''
        Basically equivalent to range function of python, except order of arguments is different
        
        E.g.: "[i for i in ArithmeticSeries.gen(3)]", gives 
        [1, 2, 3]
        
        and "[i for i in ArithmeticSeries.gen(3, 0, 2)]", gives 
        [0, 2, 4]
        '''
        return super().gen([first_term, common_difference], general_term=arithmetic, start=1, end=n)

class GeometricSeries(Series):
    '''
    Creates geometric series with first term first_term 
    and common ratio common_ratio
    '''
    def __init__(self, first_term=1, common_ratio=1):
        '''
        we set the term_function to geometric
        the sum function to a×(rⁿ-1)/(r-1) (this makes taking the sum 𝓞(1) instead of 𝓞(n))
        '''
        self.term_function = geometric
        self.params = []
        self.params.append(first_term)
        self.params.append(common_ratio)
        self.sum_function = geometric_sum
        self.term_str = "tᵢ=a×rⁿ⁻¹, i∈ {1,2 …}".replace("a", str(round(first_term, 2))).replace("r", str(round(common_ratio, 2)))
        self.sum_str = "Sᵢ=a×(rⁿ-1)/r-1, n∈ {1,2 …}".replace("a", str(round(first_term, 2))).replace("r-1", str(round(common_ratio-1, 2))).replace("r", str(round(common_ratio, 2)))

    @classmethod
    def gen(cls, n, first_term=1, common_ratio=2):
        '''
        Basically equivalent to range function of python, except order of arguments is different
        
        E.g.: "[i for i in GeometricSeries.gen(3)]", gives 
        [1, 2, 4]
        
        and "[i for i in GeometricSeries.gen(3, 3, 3)]", gives 
        [3, 9, 27]
        '''
        return super().gen([first_term, common_ratio], general_term=geometric, start=1, end=n)

class HarmonicSeries(Series):
    pass 
