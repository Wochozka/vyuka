#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input("Zadej cislo:"))

if n > 10:
    n = 10

for a in range(n):
    print("{0}".format("*"*(n-a)))

