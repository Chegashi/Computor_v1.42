# from math import ab
from cmath import sqrt as sqrt
from fractions import Fraction as frac

def printMonomial(coefficient, exponent) :
    monomial = ''
    if (coefficient < 0) :
        monomial += '- ' + str(- coefficient)
    else :
        monomial +=  str(coefficient)
    monomial +=  ' * X^' + str(exponent)
    return monomial

def printComplexNumber(z):
    s = "%.3f" % z.real
    if (z.imag < 0) :
        s += ' - i * ' + "%.3f" % (-z.imag)
    else:
        s += ' + i * ' + "%.3f" % z.imag
    return(s)
    

class polynom:
    def __init__(self, s):
        self.a = s[2]
        self.b = s[1]
        self.c = s[0]
        self.delta = self.b ** 2 - 4 * self.a * self.c
        self.ReducedForm()
        self.Degree()
        self.solution()
    def ReducedForm(self):
        ReducedForm = printMonomial(self.c, 0)
        if (self.b < 0) :
            ReducedForm += ' ' + printMonomial(self.b, 1)
        else :
            ReducedForm += ' + ' + printMonomial(self.b, 1)
        if (self.a < 0) :
            ReducedForm += ' ' + printMonomial(self.a, 2)
        else :
            ReducedForm += ' + ' + printMonomial(self.a, 2)
        print('Reduced form: {}'.format(ReducedForm))

    def Degree(self):
        if (self.a) :
            degree = 2
        elif (self.b) :
            degree = 1
        else:
            degree = 0
        print ('Polynomial degree: {}'.format(degree))

    def solution(self) :
        if (self.a != 0) :
            if (self.delta == 0) :
                self.X1 = self.X2 = -self.b / (2 * self.a)
                print ('Discriminant Δ = 0 is null, the only solution are: {} = {}'.format(self.X1, frac(str(self.X1))))
            else :
                self.X1 = (-self.b - sqrt(self.delta)) / (2 * self.a)
                self.X2 = (-self.b + sqrt(self.delta)) / (2 * self.a)
                if (self.delta > 0) :
                    print('Discriminant Δ = {} is strictly positive , the two solutions are:'.format(self.delta))
                else:
                    print ('Discriminant Δ = {} is strictly negative, the two imaginaires solutions are:'.format(self.delta))
                print(printComplexNumber(self.X1))
                print(printComplexNumber(self.X2))
        else :
            if (self.b != 0) :
                self.X1 = self.X2 = -self.c / (2 * self.b)
            else :
                if (self.c == 0) :
                    self.X1 = self.X2 = 'IR Reals numbers'
                else :
                    self.X1 = self.X2 = '∅ Empty set'
            print('The solution is:\n{}'.format(self.X1))
 