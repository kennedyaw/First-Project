# Kennedy Watson
#SCIS 111-113
# Lottery Set
""" this is a code that picks 6 unique numbers from 1 to 36, inclusive for a lottery. use a set to avoid duplicates"""

import random

def main():
    numbers = set()                             # create an empty set
    while len(numbers) != 6:
        numbers.add(random.randint(1, 36))
        print(numbers)

main()
    
