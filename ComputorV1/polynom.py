#!/goinfre/mochegri/miniconda3/envs/42AI-mochegri/bin/python3

from colorama import Fore, Back, Style
import numpy as np
import matplotlib.pyplot as plt
import os

def printMonomial(coefficient, exponent) :
    if coefficient == 0:
        return ''
    monomial = ''
    if (coefficient < 0) :
        monomial += '- {:g}'.format(-coefficient)
    else :
            monomial += '+ {:g}'.format(coefficient)
    monomial +=  ' * X^{:g} '.format(exponent)
    return monomial

def printComplexNumber(z):
    s = "{:g}".format(z.real)
    if (z.imag):
        if (z.imag < 0) :
            s += " - i * {:g}".format(-z.imag)
        else:
            s += " + i * {:g}".format(z.imag)
    return(s)
    

class polynom:
    def __init__(self, s):
        if os.path.isfile('s.png'):
            os.remove('s.png')
        self.s = s
        self.ReducedForm()
        self.Degree()
        self.delta = self.s[1] ** 2 - 4 * self.s[2] * self.s[0]
        print('Δ = b^2 - 4 * a * c = {:g}^2 - 4 * ({:g}) * ({:g}) = {}{:g}{}'
              .format(self.s[1],self.s[2], self.s[0], Fore.YELLOW, self.delta,
                      Style.RESET_ALL))
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
                print('Discriminant Δ = 0 is null, the only solution are:')
                print('X = -b / (2 * a) = - ({})/ 2 * {} = {}{}{}'
                      .format(self.s[1], self.s[2], Fore.YELLOW, self.X1,
                              Style.RESET_ALL))
            else :
                if (self.delta < 0):
                    print ('Discriminant Δ = {} is'\
                        'strictly negative, the two imaginaires solutions are:'
                        .format(self.delta))
                    self.X1 = (-self.s[1] - complex(0, (-self.delta)**(1/2)))\
                        / (2 * self.s[2])
                    self.X2 = (-self.s[1] + complex(0, (-self.delta)**(1/2)))\
                        / (2 * self.s[2])
                else:
                    print('Discriminant Δ = {} is strictly positive' \
                        ', the two solutions are:'.format(self.delta))
                    self.X1 = (-self.s[1] - self.delta**(1/2)) / (2 * self.s[2])
                    self.X2 = (-self.s[1] + self.delta**(1/2)) / (2 * self.s[2])
                print('X1 = (-b - √Δ) / (2 * a) = - ({}) - √({}) / 2 * ({})' \
                    '= {}{}{}'.format(self.s[1], self.delta, self.s[2],
                                      Fore.YELLOW, printComplexNumber(self.X1),
                                      Style.RESET_ALL))
                print('X2 = (-b + √Δ) / (2 * a) = - ({}) + √({}) / 2 * ({})' \
                    '= {}{}{}'.format(self.s[1], self.delta, self.s[2],
                                      Fore.YELLOW, printComplexNumber(self.X2),
                                      Style.RESET_ALL))
        else :
            if (self.s[1] == 0 and self.s[0] == 0) :
                print('The solution is:\n', Fore.YELLOW, 'R Reals numbers.',
                      Style.RESET_ALL)
            elif (self.s[1] == 0 and self.s[0] != 0) :
                print('The solution is:\n', Fore.YELLOW,'∅ Empty set',
                      Style.RESET_ALL)
            else :
                print('The solution is:\nX = -c / b = {} / {} = {}{:.5}{}'
                      .format(-self.s[0], self.s[1], Fore.YELLOW,
                              -self.s[0] / self.s[1], Style.RESET_ALL))

    def plot(self):
        a,b = 0,0
        if (self.s[2] != 0) :
            if (self.delta == 0) :
                a, b = int(self.X1 - 5), int(self.X1 + 5)
            else :
                if (self.delta > 0):
                    a, b = int(2 * self.X1.real - self.X2.real),\
                    int(2 * self.X2.real - self.X1.real)
                else:
                    if (self.X1.real == self.X2.real):
                        a, b = int(self.X1.real - 5), int(self.X1.real + 5) +1
            coefficients = [self.s[2], self.s[1], self.s[0]]
            x = np.linspace(a, b, 100)
            y = np.polyval(coefficients, x)
            plt.plot(x, y)
            y = np.polyval([0, 0, 0], x)
            plt.plot(x, y)
            plt.savefig('s.png')
  