#!/bin/env python
import math

def main():
    p = int(input())
    # x, y, C
    charges = 0
    lines = []
    ngps = [[(x, p - y) for x in range(p + 1)] for y in range(p + 1)]

    ship = [int(inp) for inp in input().strip().split(" ")]
    longest_dist = max(ship[0], ship[1], p - ship[0], p - ship[1])
    for i in range(1, longest_dist + 1):
        #print(f"Ring {i}")
        ret = scan_ring(ship, i, ngps, lines)
        charges += ret[0]
        lines = ret[1]
    print(charges)


def scan_ring(ship, ringn, ngps, lines):
    charges = 0
    startpoint = (ship[0] - ringn, ship[1] - ringn)

    # Bottom line
    #print("Bottom Line")
    for dx in range(0, 2 * ringn + 1):
        ret = test_vertex(startpoint, ship, ngps, charges, lines, dx, 0)
        charges = ret[0]
        lines = ret[1]
    
    # Left Line
    #print("left line")
    for dy in range(1, 2 * ringn + 1):
        ret = test_vertex(startpoint, ship, ngps, charges, lines, 0, dy)
        charges = ret[0]
        lines = ret[1]

    # Top Line
    #print("top line")
    for dx in range(1, 2 * ringn + 1):
        ret = test_vertex(startpoint, ship, ngps, charges, lines, dx, 2 * ringn)
        charges = ret[0]
        lines = ret[1]

    # Right Line
    #print("right line")
    for dy in range(1, 2 * ringn):
        ret = test_vertex(startpoint, ship, ngps, charges, lines, 2 * ringn, dy)
        charges = ret[0]
        lines = ret[1]

    return (charges, lines)


def test_vertex(startpoint, ship, ngps, charges, lines, dx, dy):
    try:
        vertex = ngps[startpoint[0] + dx][startpoint[1] + dy]
        #print(f"Testing {vertex}...")

        # (m, c, x larger than ship)
        boolval = False
        if vertex[0] > ship[0]:
            boolval = True
        elif vertex[0] == ship[0] and vertex[1] < ship[1]:
            boolval = True

        line = get_line(ship, vertex, boolval)

        if line not in lines:
            #print(f"Charge laid at {vertex}")
            charges += 1 
            lines.append(line)
    finally:
        return (charges, lines)
 


def get_line(coords1, coords2, boolval):
    if coords1[0] - coords2[0] == 0:
        m = math.inf
    else:
        m = (coords1[1] - coords2[1]) / (coords1[0] - coords2[0])
    c = coords1[1] - m * coords1[0]
    return (m, c, boolval)


if __name__ == "__main__":
    main()

