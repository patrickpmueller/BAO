#!/bin/env python

from fractions import Fraction
import math

def scan_ring(ship, ringn, ngps, trigs):
    startpoint = (ship[0] - ringn, ship[1] - ringn)

    # Bottom line
    print("Bottom Line")
    for dx in range(0, 2 * ringn + 1):
        trigs = test_vertex(startpoint, ship, ngps, trigs, dx, 0)
    
    # Left Line
    print("left line")
    for dy in range(1, 2 * ringn + 1):
        trigs = test_vertex(startpoint, ship, ngps,trigs, 0, dy)

    # Top Line
    print("top line")
    for dx in range(1, 2 * ringn + 1):
        trigs = test_vertex(startpoint, ship, ngps, trigs,  dx, 2 * ringn)

    # Right Line
    print("right line")
    for dy in range(1, 2 * ringn):
        trigs = test_vertex(startpoint, ship, ngps, trigs, 2 * ringn, dy)

    return trigs

def test_vertex(startpoint, ship, ngps, trigs, dx, dy):
    try:
        vertex = ngps[startpoint[0] + dx][startpoint[1] + dy]
        print(f"Testing {vertex}...")

        line = get_line(ship, vertex)
        simplest = line[0].as_integer_ratio()
        print(f"vertex: {vertex}, m: {line[0]}, c: {line[1]}")

        if (simplest[1], simplest[0] + line[1]) == vertex:
            trigs += 1
    finally:
        return trigs 

def get_line(coords1, coords2):
    if coords1[0] - coords2[0] == 0:
        m = Fraction(math.inf)
    else:
        m = Fraction(coords1[1] - coords2[1], coords1[0] - coords2[0])
    c = coords1[1] - m * coords1[0]
    return (m, c)


p = 998 
ngps = [[(x, p - y) for x in range(p + 1)] for y in range(p + 1)]

print(scan_ring((0,0), p - 1, ngps, 0) + 2 * 999)


