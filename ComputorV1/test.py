import re

def is_polynomial(s):
    s = s.replace(' ', '')
    p = {'0': 0, '1': 0, '2': 0}
    matches = re.findall(r'(?:^[+-]?|[+-])(?:\d+(?:\.\d+)?\*X\^\d+)', s)
    for monomial in matches:
        coefficient = float(monomial.split('*')[0])
        exponent = int(monomial.split('^')[1])
        if exponent in p.keys():
            p[exponent] += coefficient
        else:
            p[exponent] = coefficient
    return p
        
is_polynomial("63685*X^0")
is_polynomial("+556665*X^0")
is_polynomial("-5.687*X^0")
is_polynomial("")
is_polynomial("X")
is_polynomial("5X")
is_polynomial("5X^")
is_polynomial("X^03")
is_polynomial("5^02")
is_polynomial("-5.22225*X^370 + 5333.5*X^30 - 4*X^20")
is_polynomial("-5.22225*X^3 + 5333.5*X^3 - 4*X^2")
00