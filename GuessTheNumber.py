#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def guess(x):
    random_number = random.randint(1, x)
    number = 0
    while random_number != number:
        number = int(input("Wprowadz liczbe: "))
        if number > random_number:
            print("Sprobuj ponownie, liczba jest za wysoka. ")
        elif number < random_number:
            print("Sprobuj ponownie, liczba jest za niska. ")
    print("Gratulacje odgadles liczbe! ")


guess(9)
