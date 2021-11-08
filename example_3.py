#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from input_to_int import *
from input_to_float import *

if __name__ == '__main__':
    n = input_to_int("Value of n? ")
    x = input_to_float("Value of x? ")

    S = 0.0

    for k in range(1, n + 1):
        a = math.log(k * x) / (k * k)
        S += a

    print(f"S = {S}")
