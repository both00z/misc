'''
Simple implementation of Shunting-yard algorithm and reverse Polish notation
'''

import re
import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_operator(token):
    return token in ['+', '-', '*', '/', '^', '%']

def is_left_associative(operator):
    return operator in ['+', '-', '*', '/', '^', '%']

'''
Check the precedence of mathematical operators
'''
def check_precedence(o1, o2):
    weights = {'^': 2, '*':1, '/':1, '%':1, '+':0, '-':0}
    w1 = weights[o1]
    w2 = weights[o2]

    if (w1 > w2):
        return 1
    elif (w1 == w2):
        return 0
    else:
        return -1

'''
Process the reverse Polish notation array to get the result
'''
def evaluate_eq(arr):
    stack = []
    
    for val in arr:
        if is_number(val):
            stack.append(int(val))
        else:
            v1 = stack.pop()
            v2 = stack.pop()
            
            if val == '+':
                stack.append(v2 + v1)
            elif val == '-':
                stack.append(v2 - v1)
            elif val == '*':
                stack.append(v2 * v1)
            elif val == '/':
                stack.append(v2 / v1)
            elif val == '^':
                stack.append(math.pow(v2, v1))
            elif val == '%':
                stack.append(v2 % v1)

    return stack[0]

'''
Use shunting yard algorithm to convert string eq into reverse Polish notation represented as an array
'''
def parse_eq(eq):    
    out = []
    op = []
    
    while len(eq) > 0:        
        m = re.match(r'\s*(\d+|[\(\)+/*%\^\-])\s*(.*)', eq)

        token = m.group(1)
        eq = m.group(2)

        if is_number(token):
            out.append(token)
        elif is_operator(token):
            while len(op)>0:
                o2 = op[-1]
                if o2 == '(':
                    break;
                elif is_left_associative(token) and check_precedence(token, o2) <= 0:
                    op.pop()
                    out.append(o2)
                else:
                    break
            op.append(token)
        elif token == '(':
            op.append(token)
        elif token == ')':
            while len(op)>0:
                o2 = op[-1]
                if o2 != '(':
                    op.pop()
                    out.append(o2)
                else:
                    op.pop()
                    break

    while len(op) > 0:
        o = op.pop()
        out.append(o)

    return out

'''
Main method - evaluates a human-readable equation
'''
def e(eq):
    arr = parse_eq(eq)
    return evaluate_eq(arr)

equation = raw_input('enter equation: ')
print(e(equation))
