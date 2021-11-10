#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from input_to_int import input_to_int

# Задание 2
# Определить, есть ли среди трёх заданных чисел нечётные

if __name__ == '__main__':
    a = input_to_int("a")
    b = input_to_int("b")
    c = input_to_int("c")

    if (a + b) % 2 != 0:
        print('Odd')

    elif (b + c) % 2 != 0:
        print('Odd')

    elif (a + c) % 2 != 0:
        print('Odd')

    else:
        print('Even')