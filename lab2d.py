#!/usr/bin/env python3

import sys


if len(sys.argv) != 3:
    print("Usage: {} name age".format(sys.argv[0]))
    sys.exit()


name = sys.argv[1]

age = sys.argv[2]


print("Hi {}, you are {} years old.".format(name, age))


