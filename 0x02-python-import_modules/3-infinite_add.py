#!/usr/bin/python3

if __name__ == "__main__":

    """add all numbers of the argument"""
    import sys

    num = 0
    count = len(sys.argv) - 1
    for i in range(count):
        num = num + int(sys.argv[i + 1])
    print("{}".format(num))
