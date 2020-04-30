#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    i = 1
    suma = 0
    while (i < len(argv)):
        suma = suma + (int(argv[i]))
        i += 1
    print("{}".format(suma))
