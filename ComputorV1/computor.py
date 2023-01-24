#!/goinfre/mochegri/miniconda3/envs/42AI-mochegri/bin/python3
from colorama import Fore, Back, Style
from polynom import polynom
from sys import argv
import re

def parseEquation(equation):
    equation = equation.replace(' ', '')
    polynoms = equation.split('=')
    if (len(polynoms) != 2) :
        print(Fore.RED, 'invalide equation', Style.RESET_ALL)
        exit(1)
    return reduce(polynoms[0], polynoms[1])

def reduce(l, r):
    p = {0: 0, 1: 0, 2: 0}
    patern = r'(?:^[+-]?|[+-])(?:\d+(?:\.\d+)?\*X\^\d+)'
    matches_l = re.findall(patern, l)
    matches_r = re.findall(patern, r)
    for monomial in matches_l:
        coefficient = float(monomial.split('*')[0])
        exponent = int(monomial.split ('^')[1])
        if (exponent in p.keys()):
            p[exponent] = coefficient + p[exponent]
        else:
            p[exponent] = coefficient
    for monomial in matches_r:
        coefficient = float(monomial.split('*')[0])
        exponent = int(monomial.split('^')[1])
        if (exponent in p.keys()):
            p[exponent] = - coefficient + p[exponent]
        else:
            p[exponent] = -coefficient
    return p

def main():
    if (len(argv) == 2) :
        equation = argv[1]
    elif (len(argv) == 1) :
        equation = input('Enter an equation: ')
    else :
        print(Fore.RED, 'multiple arguments', Style.RESET_ALL)
        exit(1)
    p = polynom(parseEquation(equation)) # [a, b, c] ==  c + bx + ax^2 

if __name__ == "__main__":
    main()

