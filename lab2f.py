#!/usr/bin/env python3
# Author: SAMBHAV SACHDEVA
# Author ID: 166945220
# Date Created: 2024/05/23

import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} timer")
    sys.exit(1)

# Assign the command-line argument to the timer variable
timer = int(sys.argv[1])

# While loop that counts down from the timer value to 1
while timer > 0:
    print(timer)
    timer -= 1

# Print the final message
print("blast off!")