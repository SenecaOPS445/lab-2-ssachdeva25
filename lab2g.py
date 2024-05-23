#!/usr/bin/env python3
# Author: Sambhav Sachdeva
# Author ID: 166945220
# Date Created: 2024/05/23

import sys

# Check if an argument is provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

# While loop that counts down from the timer value to 1
while timer > 0:
    print(timer)
    timer -= 1

# Print the final message
print("blast off!")
