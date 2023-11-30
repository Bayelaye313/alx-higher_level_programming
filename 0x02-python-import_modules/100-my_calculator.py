#!/usr/bin/python3
import sys
from calculation_1 import add, sub, div, mul

def print_usage_and_exit():
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

def print_unknown_operator_and_exit():
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

if __name__ == '__main__':
    i = len(sys.argv) - 1
    if i != 3:
        print_usage_and_exit()

    a, ops, b = map(int, sys.argv[1:])
    
    if ops == '+':
        result = add(a, b)
    elif ops == '-':
        result = sub(a, b)
    elif ops == '*':
        result = mul(a, b)
    elif ops == '/':
        if b == 0:
            print("Error: Division by zero")
            sys.exit(1)
        result = div(a, b)
    else:
        print_unknown_operator_and_exit()

    print("{} {} {} = {}".format(a, ops, b, result))
