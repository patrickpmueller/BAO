#!/bin/env python
import rotor

possible_shifts = []
target = 0
length = 2**23

baseline =  "0" * length

for first_pos_1 in range(length):
    possible_shift = baseline[:first_pos_1] + "1" + baseline[first_pos_1 + 1:]
    for second_pos_1 in range(1 + first_pos_1, length):
        full_pos_shift = possible_shift[:second_pos_1] + "1" + possible_shift[second_pos_1 + 1:]
        print(f"Testing (first 15 digits): {full_pos_shift[0:15]}, Progress: {((first_pos_1 + 1) * (second_pos_1 + 1)) / (length ** 2) * 100}")
        check = rotor.turn_rotor(full_pos_shift, baseline, 1, length)
        if rotor.xor(check, 0) == 0:
            target += 1
