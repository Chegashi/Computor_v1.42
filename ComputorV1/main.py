from polynom import polynom
from sys import argv
import re

def parseEquation(equation):
    polynoms = equation.split('=')
    if (len(polynoms) != 2) :
        print('invalide equation ')
        exit(1)
    Side = reduce(polynoms[0], polynoms[1])
    print('Side = ', Side)

def reduce(l, r):
    l = l.replace(' ', '')
    p = {0: 0, 1: 0, 2: 0}
    matches_l = re.findall(r'(?:^[+-]?|[+-])(?:\d+(?:\.\d+)?\*X\^\d+)', l)
    matches_r = re.findall(r'(?:^[+-]?|[+-])(?:\d+(?:\.\d+)?\*X\^\d+)', r)
    for monomial in matches_l:
        coefficient = float(monomial.split('*')[0])
        exponent = int(monomial.split('^')[1])
        if exponent in p.keys():
            p[exponent] += coefficient
        else:
            p[exponent] = coefficient
    for monomial in matches_r:
        coefficient = float(monomial.split('*')[0])
        exponent = int(monomial.split('^')[1])
        if exponent in p.keys():
            p[exponent] += - coefficient
        else:
            p[exponent] = - coefficient
    return p

def main():
    if (len(argv) == 2) :
        equation = argv[1]
    elif (len(argv) == 1) :
        equation = input('Enter an equation: ')
    else :
        print('multiple arguments\n')
        exit(1)
    parseEquation(equation)
    p = polynom([3, 2, 3]) # [a, b, c] == ax^2 + bx + c

if __name__ == "__main__":
    main()

