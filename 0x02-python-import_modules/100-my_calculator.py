#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    numer = int(argv[1])
    oper = int(argv[3])
    if (argv[2] == "+"):
        print("{} + {} = {}".format(numer, oper, add(numer, oper)))
    elif (argv[2] == "-"):
        print("{} - {} = {}".format(numer, oper, sub(numer, oper)))
    elif (argv[2] == "*"):
        print("{} * {} = {}".format(numer, oper, mul(numer, oper)))
    elif (argv[2] == "/"):
        print("{} / {} = {}".format(numer, oper, div(numer, oper)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
