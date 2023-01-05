from cmath import sqrt as sqrt
from math import trunc
from fractions import Fraction as frac

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
        self.s = s
        self.delta = self.s[1] ** 2 - 4 * self.s[2] * self.s[0]
        self.ReducedForm()
        self.Degree()
        self.solution()

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
                print ('Discriminant Δ = 0 is null, the only solution are:\n{}'.format(frac(str(self.X1))))
            else :
                self.X1 = (-self.s[1] - sqrt(self.delta)) / (2 * self.s[2])
                self.X2 = (-self.s[1] + sqrt(self.delta)) / (2 * self.s[2])
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
 