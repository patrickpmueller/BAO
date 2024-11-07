#!/bin/env python

def main():
    shift = input()
    check = input()
    r = int(input())

    print(turn_rotor(shift, check, r, len(shift)))


def turn_rotor(shift, check, r, n):
    for i in range(n):
        shift = rotate(shift, r)
        cval = c(shift[0], shift[-1], check[i])
        check = check[:i] + cval + check[i + 1:]
    
    return check
 

def c(s0, s1, ci):
    return xor(xor(s0, s1), ci)


def rotate(shift, r):
    for ri in range(abs(r)):
        if r > 0:
            shift = shift[1:] + shift[0]
        else:
            shift = shift[-1] + shift[:-1]
    return shift


def xor(a, b):
    n1 = 0
    total = a + b

    for char in total:
        if char == "1":
            n1 += 1
    return str(n1 % 2)


if __name__ == "__main__":
    main()
