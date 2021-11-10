#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from input_to_int import input_to_int

# Задание 1
# 1. Дано натуральное число . Вывести на экран фразу Мне n лет , учитывая, что при
# некоторых значениях n слово «лет» надо заменить на слово «год» или «года».

if __name__ == '__main__':
    m = input_to_int("n (let)")
    n = m % 100

    if (n > 10) and (n < 15):  # Исключением .11 .12 .13 .14
        print(f'Mne {m} let')
    else:
        n = n % 10

        if n == 1:  # .1 - год
            print(f'Mne {m} god')
        elif (n > 1) and (n < 5):  # .2 .3 .4 - года
            print(f'Mne {m} goda')
        else:  # .0 .5 .6 .7 .8 .9 - лет
            print(f' {m} let')
