#!/goinfre/mochegri/miniconda3/envs/42AI-mochegri/bin/python3
from cmath import sqrt as sqrt
from math import trunc
from fractions import Fraction as frac
import numpy as np
import matplotlib.pyplot as plt
import os

def printMonomial(coefficient, exponent) :
    if coefficient == 0:
        return ''
    monomial = ''
    if (coefficient < 0) :
        if (coefficient != trunc(coefficient)):
            monomial += '- ' + '%.2f' % (-coefficient)
        else:
            monomial += '- ' + '%d' % (trunc(-coefficient))
    else :
        if (coefficient != trunc(coefficient)):
            monomial += '+ ' + '%.2f' % (coefficient)
        else:
            monomial += '+ ' + '%d' % (trunc(coefficient))
    monomial +=  ' * X^' + '%d' % (exponent) + ' '
    return monomial

def printComplexNumber(z):
    if (z.real != trunc(z.real)):
        s = "%.6f" % z.real
    else:
        s = trunc(z.real)
    if (z.imag):
        if (z.imag < 0) :
            s += ' - i * ' + "%.3f" % (-z.imag)
        else:
            s += ' + i * ' + "%.3f" % z.imag
    return(s)
    

class polynom:
    def __init__(self, s):
        if os.path.isfile('s.png'):
            os.remove('s.png')
        self.s = s
        self.ReducedForm()
        self.Degree()
        self.delta = self.s[1] ** 2 - 4 * self.s[2] * self.s[0]
        print('Δ = b^2 - 4 * a * c = {}^2 - 4 * {} * {} = {}'.format(self.s[1],self.s[2], self.s[0], self.delta))
        self.solution()
        self.plot()

    def ReducedForm(self):
        ReducedForm = ''
        for i in self.s:
            ReducedForm += printMonomial(self.s[i], i)
        if ReducedForm[0:2] == '+ ':
            ReducedForm = ReducedForm[2:]
        if (ReducedForm):
            print('Reduced form: {}= 0'.format(ReducedForm))
        else:
            print('Reduced form: 0X = 0')

    def Degree(self):
        degree = 0
        for mono in self.s :
            if degree < mono and self.s[mono]:
                degree = mono
        print ('Polynomial degree: {}'.format(degree))
        if (degree > 2):
            print('The polynomial degree is strictly greater than 2, I can\'t solve.')
            exit(1)

    def solution(self) :
        if (self.s[2] != 0) :
            if (self.delta == 0) :
                self.X1 = self.X2 = -self.s[1] / (2 * self.s[2])
                print('Discriminant Δ = 0 is null, the only solution are:\n{}'.format(frac(str(self.X1))))
                print('X = -b / (2 * a) = - ({})/ 2 * {} = '.format(self.s[1], self.s[2]))
            else :
                self.X1 = (-self.s[1] - sqrt(self.delta)) / (2 * self.s[2])
                self.X2 = (-self.s[1] + sqrt(self.delta)) / (2 * self.s[2])
                print('X1 = (-b - √Δ) / (2 * a) = - ({}) - √({}) / 2 * ({}) = {}'.format(self.s[1], self.delta, self.s[2], printComplexNumber(self.X1)))
                print('X2 = (-b + √Δ) / (2 * a) = - ({}) + √({}) / 2 * ({}) = {}'.format(self.s[1], self.delta, self.s[2], printComplexNumber(self.X2)))
                if (self.delta > 0) :
                    print('Discriminant Δ = {} is strictly positive , the two solutions are:'.format(self.delta))
                else:
                    print ('Discriminant Δ = {} is strictly negative, the two imaginaires solutions are:'.format(self.delta))
                print(printComplexNumber(self.X1))
                print(printComplexNumber(self.X2))
        else :
            if (self.s[1] == 0 and self.s[0] == 0) :
                self.X1 = self.X2 = 'IR Reals numbers'
            elif (self.s[1] == 0 and self.s[0] != 0) :
                self.X1 = self.X2 = '∅ Empty set'
            else :
                self.X1 = self.X2 = -self.s[0] / self.s[1]
            print('The solution is:\n{}'.format(self.X1))

    def plot(self):
        a,b = 0,0
        if (self.s[2] != 0) :
            if (self.delta == 0) :
                a, b = trunc(self.X1 - 5), trunc(self.X1 + 5)
            else :
                if (self.delta > 0):
                    a, b = trunc(2 * self.X1.real - self.X2.real), trunc(2 * self.X2.real - self.X1.real)
                else:
                    if (self.X1.real == self.X2.real):
                        a, b = trunc(self.X1.real - 5), trunc(self.X1.real + 5) +1
            coefficients = [self.s[2], self.s[1], self.s[0]]
            x = np.linspace(a, b, 100)
            y = np.polyval(coefficients, x)
            plt.plot(x, y)
            y = np.polyval([0, 0, 0], x)
            plt.plot(x, y)
            plt.savefig('s.png')
  