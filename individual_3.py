#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from input_to_int import input_to_int

# Задание 2
# Найти сумму целых положительных чисел, больших 20, меньших 100 и кратных 3.

if __name__ == '__main__':

    summa = 0

    for n in range(20, 100):
        if n % 3 == 0:
            summa += n

    print(f"Sum = {summa}")
