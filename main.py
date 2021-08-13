#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def guess(x):
    random_number = random.randint(1,x)
    number = 0
    while random_number != number:
        number = input("Zgdanij numer z przedziału 1 do {x}")
        if number > random_number:
            print("Spróbuj ponownie, liczba jest za wysoka. ")
        elif number < random_number:
            print("Spróbuj ponownie, liczba jest za niska. ")
    print("Gratulacje odgadłeś liczbę! ")

    guess(17)
