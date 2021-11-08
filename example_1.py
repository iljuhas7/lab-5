#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    x = float(input("Value of x? "))

    if x <= 0:
        print(f"x < 0 or x = 0 then")
        print(f"y = 2 * ({x} * {x}) + cos({x})")
        y = 2 * x * x + math.cos(x)
    elif x < 5:
        print(f"x < 5")
        print(f"y = 2 * ({x} * {x}) + cos({x})")
        y = x + 1
    else:
        print(f"x > 5 or x = 5 then")
        print(f"y = 2 * ({x} * {x}) + cos({x})")
        y = math.sin(x) - x * x

    print(f"y = {y:.2f}")
