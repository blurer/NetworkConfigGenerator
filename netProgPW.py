#!/usr/bin/env python3
import string
import random

length = 16
qty = 1

for y in range(qty):
    password = ''
    for c in range(length):
        password += random.choice(string.hexdigits)
    print(password)



